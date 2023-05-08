#!/usr/bin/env python3.11

from admon_mode_cps_pkg.registry.registry import Registry
from python_statemachine.statemachine import State
from python_statemachine.statemachine import StateMachine


def create_mm(registry: Registry):
    """Creates a mode manager for each device and returns them as a dict"""
    mm_list = {}
    for device in registry.device_list:
        mm_list[device.name] = TBModeManager()
    return mm_list


class TBModeManager(StateMachine):
    """Yields the modes for a ROS TurtleBot"""

    # modes
    defaultMode = State("default operation", initial=True)
    maintenanceMode = State("ongoing maintenance")
    preSafetyMode = State("precautious mode for collision avoidance")

    # transitions to other modes
    startMaintenance = defaultMode.to(maintenanceMode)
    stopMaintenance = maintenanceMode.to(defaultMode)
    startSafeMode = defaultMode.to(preSafetyMode)
    stopSafeMode = preSafetyMode.to(defaultMode)
