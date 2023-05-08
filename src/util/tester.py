"""These methods create test data for the default multi_turtlebot3 scenario shipped per default by ROS"""
from app.registry.device_registry import Device
from app.registry.registry import Registry
from app.registry.zone_registry import Zone
from app.util.util import generate_uuid


def get_test_devices(zone_list) -> list[Device]:
    turtlebot_1 = Device(device_id='tb3_0', zone_id=zone_list[0], name='tb3_0')
    turtlebot_2 = Device(device_id='tb3_1', zone_id=zone_list[3], name='tb3_1')
    turtlebot_3 = Device(device_id='tb3_2', zone_id=zone_list[5], name='tb3_2')
    turtlebot_1.can_move_freely()
    return [turtlebot_1, turtlebot_2, turtlebot_3]


def get_test_zones() -> list[Zone]:
    zone1 = Zone(zone_id=generate_uuid(), name='zone_1', description='start zone of tb3_0')
    zone2 = Zone(zone_id=generate_uuid(), name='zone_2')
    zone3 = Zone(zone_id=generate_uuid(), name='zone_3')
    zone4 = Zone(zone_id=generate_uuid(), name='zone_4', description='start zone of tb3_2')
    zone5 = Zone(zone_id=generate_uuid(), name='zone_5')
    zone6 = Zone(zone_id=generate_uuid(), name='zone_6', description='start zone of tb3_1')
    return [zone1, zone2, zone3, zone4, zone5, zone6]


def get_test_registry() -> Registry:
    zone_list = get_test_zones()
    device_list = get_test_devices(zone_list)
    return Registry(zone_list=zone_list, device_list=device_list)
