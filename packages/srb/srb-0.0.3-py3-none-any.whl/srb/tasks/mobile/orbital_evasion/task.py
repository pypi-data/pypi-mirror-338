from dataclasses import MISSING
from typing import Sequence, Tuple

import torch

from srb._typing import StepReturn
from srb.core.asset import RigidObjectCollection, RigidObjectCollectionCfg
from srb.core.env import OrbitalEnv, OrbitalEnvCfg, OrbitalEventCfg, OrbitalSceneCfg
from srb.core.manager import EventTermCfg, SceneEntityCfg
from srb.core.marker import VisualizationMarkers, VisualizationMarkersCfg
from srb.core.mdp import reset_collection_root_state_uniform_poisson_disk_3d
from srb.core.sim import PreviewSurfaceCfg, SphereCfg
from srb.utils.cfg import configclass

from .asset import select_obstacle

##############
### Config ###
##############


@configclass
class SceneCfg(OrbitalSceneCfg):
    env_spacing = 12.0

    objs: RigidObjectCollectionCfg = RigidObjectCollectionCfg(
        rigid_objects=MISSING,  # type: ignore
    )


@configclass
class EventCfg(OrbitalEventCfg):
    randomize_object_state: EventTermCfg = EventTermCfg(
        func=reset_collection_root_state_uniform_poisson_disk_3d,
        mode="reset",
        params={
            "asset_cfg": SceneEntityCfg("objs"),
            "pose_range": {
                "x": (-10.0, 10.0),
                "y": (-10.0, 10.0),
                "z": (-50.0, 10.0),
                "roll": (-torch.pi, torch.pi),
                "pitch": (-torch.pi, torch.pi),
                "yaw": (-torch.pi, torch.pi),
            },
            "velocity_range": {
                "x": (-0.1, 0.1),
                "y": (-0.1, 0.1),
                "z": (-0.1, 0.1),
                "roll": (-0.1 * torch.pi, 0.1 * torch.pi),
                "pitch": (-0.1 * torch.pi, 0.1 * torch.pi),
                "yaw": (-0.1 * torch.pi, 0.1 * torch.pi),
            },
            "radius": (5.0),
        },
    )


@configclass
class TaskCfg(OrbitalEnvCfg):
    ## Scene
    scene: SceneCfg = SceneCfg()
    num_obstacles: int = 20

    ## Events
    events: EventCfg = EventCfg()

    ## Time
    episode_length_s: float = 30.0
    is_finite_horizon: bool = False

    ## Target
    tf_pos_target: Tuple[float, float, float] = (0.0, 0.0, -50.0)
    tf_quat_target: Tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)
    target_marker_cfg: VisualizationMarkersCfg = VisualizationMarkersCfg(
        prim_path="/Visuals/target",
        markers={
            "target": SphereCfg(
                radius=0.25,
                visual_material=PreviewSurfaceCfg(emissive_color=(0.2, 0.2, 0.8)),
            )
        },
    )

    def __post_init__(self):
        super().__post_init__()

        # Scene: Asteroids
        self.scene.objs.rigid_objects = {
            f"obstacle{i}": select_obstacle(
                self,
                prim_path=f"{{ENV_REGEX_NS}}/obstacle{i}",
                seed=self.seed + (i * self.scene.num_envs),
                activate_contact_sensors=True,
            )
            for i in range(self.num_obstacles)
        }

        # Update seed & number of variants for procedural assets
        self._update_procedural_assets()


############
### Task ###
############


class Task(OrbitalEnv):
    cfg: TaskCfg

    def __init__(self, cfg: TaskCfg, **kwargs):
        super().__init__(cfg, **kwargs)

        ## Get scene assets
        self._objs: RigidObjectCollection = self.scene["objs"]
        self._target_marker: VisualizationMarkers = VisualizationMarkers(
            self.cfg.target_marker_cfg
        )

        ## Initialize buffers
        self._tf_pos_target = self.scene.env_origins + torch.tensor(
            self.cfg.tf_pos_target, dtype=torch.float32, device=self.device
        ).repeat(self.num_envs, 1)
        self._tf_quat_target = torch.tensor(
            self.cfg.tf_quat_target, dtype=torch.float32, device=self.device
        ).repeat(self.num_envs, 1)

        ## Visualize target
        self._target_marker.visualize(self._tf_pos_target, self._tf_quat_target)

    def _reset_idx(self, env_ids: Sequence[int]):
        super()._reset_idx(env_ids)

    def extract_step_return(self) -> StepReturn:
        return _compute_step_return(
            ## Time
            episode_length=self.episode_length_buf,
            max_episode_length=self.max_episode_length,
            truncate_episodes=self.cfg.truncate_episodes,
            ## Actions
            act_current=self.action_manager.action,
            act_previous=self.action_manager.prev_action,
            ## States
            # Root
            tf_pos_robot=self._robot.data.root_pos_w,
            vel_lin_robot=self._robot.data.root_lin_vel_b,
            vel_ang_robot=self._robot.data.root_ang_vel_b,
            # Transforms (world frame)
            tf_pos_objs=self._objs.data.object_com_pos_w,
            tf_pos_target=self._tf_pos_target,
            # IMU
            imu_lin_acc=self._imu_robot.data.lin_acc_b,
            imu_ang_vel=self._imu_robot.data.ang_vel_b,
        )


@torch.jit.script
def _compute_step_return(
    *,
    ## Time
    episode_length: torch.Tensor,
    max_episode_length: int,
    truncate_episodes: bool,
    ## Actions
    act_current: torch.Tensor,
    act_previous: torch.Tensor,
    ## States
    # Root
    tf_pos_robot: torch.Tensor,
    vel_lin_robot: torch.Tensor,
    vel_ang_robot: torch.Tensor,
    # Transforms (world frame)
    tf_pos_objs: torch.Tensor,
    tf_pos_target: torch.Tensor,
    # IMU
    imu_lin_acc: torch.Tensor,
    imu_ang_vel: torch.Tensor,
) -> StepReturn:
    num_envs = episode_length.size(0)
    num_objs = tf_pos_objs.size(1)
    # dtype = episode_length.dtype
    device = episode_length.device

    ############
    ## States ##
    ############
    ## Transforms (world frame)
    # Robot -> Object
    pos_robot_to_objs = tf_pos_robot.unsqueeze(1).repeat(1, num_objs, 1) - tf_pos_objs
    tf_pos_robot_to_nearest_obj = pos_robot_to_objs[
        torch.arange(pos_robot_to_objs.size(0)),
        torch.argmin(torch.norm(pos_robot_to_objs, dim=-1), dim=1),
    ]

    # Robot -> Target
    tf_pos_robot_to_target = tf_pos_robot - tf_pos_target

    #############
    ## Rewards ##
    #############
    # Penalty: Action rate
    WEIGHT_ACTION_RATE = -0.05
    penalty_action_rate = WEIGHT_ACTION_RATE * torch.sum(
        torch.square(act_current - act_previous), dim=1
    )

    # Penalty: Angular velocity
    WEIGHT_ANGULAR_VELOCITY = -0.1
    penalty_angular_velocity = WEIGHT_ANGULAR_VELOCITY * torch.norm(
        vel_ang_robot, dim=-1
    )

    # Reward: Distance | Robot <--> Object
    WEIGHT_DISTANCE_ROBOT_TO_OBJ = 1.0
    reward_distance_robot_to_nearest_obj = WEIGHT_DISTANCE_ROBOT_TO_OBJ * torch.norm(
        tf_pos_robot_to_nearest_obj, dim=-1
    )

    # Penalty: Distance | Robot <--> Target
    WEIGHT_DISTANCE_ROBOT_TO_TARGET = -32.0
    penalty_distance_robot_to_target = WEIGHT_DISTANCE_ROBOT_TO_TARGET * torch.norm(
        tf_pos_robot_to_target, dim=-1
    )

    ##################
    ## Terminations ##
    ##################
    # No termination condition
    termination = torch.zeros(num_envs, dtype=torch.bool, device=device)
    # Truncation
    truncation = (
        episode_length >= max_episode_length
        if truncate_episodes
        else torch.zeros(num_envs, dtype=torch.bool, device=device)
    )

    return StepReturn(
        {
            "state": {
                "vel_lin_robot": vel_lin_robot,
                "vel_ang_robot": vel_ang_robot,
                "tf_pos_robot_to_nearest_obj": tf_pos_robot_to_nearest_obj,
                "tf_pos_robot_to_target": tf_pos_robot_to_target,
            },
            "state_dyn": {
                "pos_robot_to_objs": pos_robot_to_objs,
            },
            "proprio": {
                "imu_lin_acc": imu_lin_acc,
                "imu_ang_vel": imu_ang_vel,
            },
            # "proprio_dyn": {},
        },
        {
            "penalty_action_rate": penalty_action_rate,
            "penalty_angular_velocity": penalty_angular_velocity,
            "reward_distance_robot_to_nearest_obj": reward_distance_robot_to_nearest_obj,
            "penalty_distance_robot_to_target": penalty_distance_robot_to_target,
        },
        termination,
        truncation,
    )
