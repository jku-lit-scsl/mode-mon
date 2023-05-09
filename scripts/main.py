#!/usr/bin/env python3.11

from threading import Thread

import rospy
from admon_mode_cps_pkg.adaption_controller.MonitoringManager import MonitoringManager
from admon_mode_cps_pkg.adaption_controller.TBModeManager import create_mm
from admon_mode_cps_pkg.util.tester import add_test_topics
from admon_mode_cps_pkg.util.tester import get_test_registry

REGISTRY = {}
MODE_M_LIST = {}

if __name__ == '__main__':

    try:
        # create registry
        REGISTRY = get_test_registry()
        # init Mode Manager
        MODE_M_LIST = create_mm(REGISTRY)
        # init Monitoring Manager
        mon_m = MonitoringManager()
        mon_m = add_test_topics(mon_m)

        # start monitoring
        mon_thread = Thread(target=mon_m.start_monitoring)
        mon_thread.start()

        # listen to mode switches
        mode_switch_thread = Thread(target=mon_m.start_mode_listener, args=(MODE_M_LIST, REGISTRY))
        mode_switch_thread.start()

    except rospy.ROSInterruptException:
        pass
