from statemachine import StateMachine, State


class TBModeManager(StateMachine):
    """Yields the modes for a ROS TurtleBot"""

    # modes
    defaultMode = State("default operation", initial=True)
    maintenanceMode = State("ongoing maintenance")

    # transitions to other modes
    startMaintenance = defaultMode.to(maintenanceMode)
    stopMaintenance = maintenanceMode.to(defaultMode)
