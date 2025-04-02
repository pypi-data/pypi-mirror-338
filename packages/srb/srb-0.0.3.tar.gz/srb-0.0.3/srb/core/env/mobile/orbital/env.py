from dataclasses import MISSING

import torch

from srb import assets
from srb.core.asset import AssetVariant, OrbitalRobot, Scenery
from srb.core.domain import Domain
from srb.core.env import ViewerCfg
from srb.core.env.mobile.env import (
    MobileEnv,
    MobileEnvCfg,
    MobileEventCfg,
    MobileSceneCfg,
)
from srb.core.manager import EventTermCfg, SceneEntityCfg
from srb.core.mdp import reset_root_state_uniform
from srb.utils.cfg import configclass


@configclass
class OrbitalSceneCfg(MobileSceneCfg):
    env_spacing = 4.0


@configclass
class OrbitalEventCfg(MobileEventCfg):
    randomize_robot_state: EventTermCfg = EventTermCfg(
        func=reset_root_state_uniform,
        mode="reset",
        params={
            "asset_cfg": SceneEntityCfg("robot"),
            "pose_range": {
                "x": (-0.2, 0.2),
                "y": (-0.2, 0.2),
                "z": (-0.2, 0.2),
                "roll": (-torch.pi, torch.pi),
                "pitch": (-torch.pi, torch.pi),
                "yaw": (-torch.pi, torch.pi),
            },
            "velocity_range": {
                "x": (-0.1, 0.1),
                "y": (-0.1, 0.1),
                "z": (-0.1, 0.1),
                "roll": (-0.7854, 0.7854),
                "pitch": (-0.7854, 0.7854),
                "yaw": (-0.7854, 0.7854),
            },
        },
    )


@configclass
class OrbitalEnvCfg(MobileEnvCfg):
    ## Scenario
    domain: Domain = Domain.ORBIT

    ## Assets
    robot: OrbitalRobot | AssetVariant = assets.Cubesat()
    _robot: OrbitalRobot = MISSING  # type: ignore
    scenery: Scenery | AssetVariant | None = None

    ## Scene
    scene: OrbitalSceneCfg = OrbitalSceneCfg()

    ## Events
    events: OrbitalEventCfg = OrbitalEventCfg()

    ## Time
    env_rate: float = 1.0 / 25.0
    agent_rate: float = 1.0 / 25.0

    ## Viewer
    viewer: ViewerCfg = ViewerCfg(
        eye=(10.0, -10.0, 10.0), lookat=(0.0, 0.0, 0.0), origin_type="env"
    )

    def __post_init__(self):
        super().__post_init__()


class OrbitalEnv(MobileEnv):
    cfg: OrbitalEnvCfg

    def __init__(self, cfg: OrbitalEnvCfg, **kwargs):
        super().__init__(cfg, **kwargs)
