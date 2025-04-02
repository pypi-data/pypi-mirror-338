from __future__ import annotations

from collections.abc import Callable
from typing import TypedDict

import mx_bluesky.hyperion.experiment_plans.flyscan_xray_centre_plan as flyscan_xray_centre_plan
import mx_bluesky.hyperion.experiment_plans.rotation_scan_plan as rotation_scan_plan
from mx_bluesky.hyperion.experiment_plans import (
    grid_detect_then_xray_centre_plan,
    load_centre_collect_full_plan,
    pin_centre_then_xray_centre_plan,
)
from mx_bluesky.hyperion.parameters.gridscan import (
    GridScanWithEdgeDetect,
    HyperionSpecifiedThreeDGridScan,
    PinTipCentreThenXrayCentre,
)
from mx_bluesky.hyperion.parameters.load_centre_collect import LoadCentreCollect
from mx_bluesky.hyperion.parameters.rotation import MultiRotationScan, RotationScan


def not_implemented():
    raise NotImplementedError


def do_nothing():
    pass


class ExperimentRegistryEntry(TypedDict):
    setup: Callable
    param_type: type[
        HyperionSpecifiedThreeDGridScan
        | GridScanWithEdgeDetect
        | RotationScan
        | MultiRotationScan
        | PinTipCentreThenXrayCentre
        | LoadCentreCollect
    ]


PLAN_REGISTRY: dict[str, ExperimentRegistryEntry] = {
    "flyscan_xray_centre": {
        "setup": flyscan_xray_centre_plan.create_devices,
        "param_type": HyperionSpecifiedThreeDGridScan,
    },
    "grid_detect_then_xray_centre": {
        "setup": grid_detect_then_xray_centre_plan.create_devices,
        "param_type": GridScanWithEdgeDetect,
    },
    "rotation_scan": {
        "setup": rotation_scan_plan.create_devices,
        "param_type": RotationScan,
    },
    "pin_tip_centre_then_xray_centre": {
        "setup": pin_centre_then_xray_centre_plan.create_devices,
        "param_type": PinTipCentreThenXrayCentre,
    },
    "multi_rotation_scan": {
        "setup": rotation_scan_plan.create_devices,
        "param_type": MultiRotationScan,
    },
    "load_centre_collect_full": {
        "setup": load_centre_collect_full_plan.create_devices,
        "param_type": LoadCentreCollect,
    },
}


class PlanNotFound(Exception):
    pass
