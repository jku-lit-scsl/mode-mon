#!/usr/bin/env python3.11

import rospy
from admon_mode_cps_pkg.registry.registry import Registry
from python_statemachine.statemachine import State
from python_statemachine.statemachine import StateMachine


def create_mm(registry: Registry):
    """Creates a mode manager for each device and returns them as a dict"""
    mm_list = {}
    for device in registry.device_list:
        mm_list[device.name] = TBModeManager(device.name)
    return mm_list


class TBModeManager(StateMachine):
    """Yields the modes for a ROS TurtleBot"""

    def __init__(self, name):
        self.mon_manager = {}
        self.name = name
        self.fq = 3.0

        super(TBModeManager, self).__init__()

    def set_mon_manager(self, mon_manager):
        self.mon_manager = mon_manager

    # modes
    defaultMode = State("default operation", initial=True)
    maintenanceMode = State("ongoing maintenance")
    preSafetyMode = State("precautious mode for collision avoidance")

    # transitions to other modes
    startMaintenance = defaultMode.to(maintenanceMode)
    stopMaintenance = maintenanceMode.to(defaultMode)
    startSafeMode = defaultMode.to(preSafetyMode)
    stopSafeMode = preSafetyMode.to(defaultMode)

    def on_enter_maintenanceMode(self):
        # adapt monitoring to maintenanceMode
        # TODO: encode in config once fully implemented
        self.fq = 1.0
        rospy.loginfo(f"new monitoring frequency for {self.name} because of maintenance")

    def on_enter_preSafetyMode(self):
        # adapt monitoring to maintenanceMode
        # TODO: encode in config once fully implemented
        self.fq = 2.0
        rospy.loginfo(f"new monitoring frequency for {self.name} for safety reasons")
