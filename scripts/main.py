#!/usr/bin/env python3.11

import rospy
from admon_mode_cps_pkg.adaption_controller.MonitoringManager import MonitoringManager
from admon_mode_cps_pkg.adaption_controller.TBModeManager import create_mm
from admon_mode_cps_pkg.util.tester import add_test_topics
from admon_mode_cps_pkg.util.tester import get_test_registry

if __name__ == '__main__':

    try:
        # create registry
        registry = get_test_registry()
        # init Mode Manager
        mode_m_list = create_mm(registry)
        # init Monitoring Manager
        mon_m = MonitoringManager()
        mon_m = add_test_topics(mon_m)
        mon_m.start_monitoring()

    except rospy.ROSInterruptException:
        pass
