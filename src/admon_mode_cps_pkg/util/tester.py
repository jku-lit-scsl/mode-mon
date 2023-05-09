"""These methods create test data for the default multi_turtlebot3 scenario shipped per default by ROS"""
from admon_mode_cps_pkg.adaption_controller.MonitoringManager import MonitoringManager
from admon_mode_cps_pkg.registry.device_registry import Device
from admon_mode_cps_pkg.registry.registry import Registry
from admon_mode_cps_pkg.registry.zone_registry import Zone
from admon_mode_cps_pkg.util.util import generate_uuid


def get_test_devices(zone_list):
    turtlebot_1 = Device(device_id='tb3_0', zone_id=zone_list[0], name='tb3_0')
    turtlebot_2 = Device(device_id='tb3_1', zone_id=zone_list[3], name='tb3_1')
    turtlebot_3 = Device(device_id='tb3_2', zone_id=zone_list[5], name='tb3_2')
    turtlebot_1.can_move_freely()
    turtlebot_2.can_move_freely()
    # turtlebot_3.can_move_freely()
    return [turtlebot_1, turtlebot_2, turtlebot_3]


def get_test_zones():
    zone1 = Zone(zone_id=generate_uuid(), name='zone_1', description='start zone of tb3_0')
    zone2 = Zone(zone_id=generate_uuid(), name='zone_2')
    zone3 = Zone(zone_id=generate_uuid(), name='zone_3')
    zone4 = Zone(zone_id=generate_uuid(), name='zone_4', description='start zone of tb3_2')
    zone5 = Zone(zone_id=generate_uuid(), name='zone_5')
    zone6 = Zone(zone_id=generate_uuid(), name='zone_6', description='start zone of tb3_1')
    return [zone1, zone2, zone3, zone4, zone5, zone6]


def get_test_registry():
    zone_list = get_test_zones()
    device_list = get_test_devices(zone_list)
    return Registry(zone_list=zone_list, device_list=device_list)


def add_test_topics(monitoring_manager: MonitoringManager):
    monitoring_manager.update_topic('/tb3_0/scan', 3.0)
    monitoring_manager.update_topic('/tb3_1/scan', 3.0)
    monitoring_manager.update_topic('/tb3_2/scan', 3.0)

    return monitoring_manager
