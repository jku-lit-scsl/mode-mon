import json
import time
from types import SimpleNamespace

import rospy
import rostopic
from admon_mode_cps_pkg.message_broker.MessageBroker import MessageBroker
from sensor_msgs.msg import LaserScan

MODE_MANAGER_LIST = {}
REGISTRY = {}


def handle_new_mon_message(data, topic_meta):
    topic_str = topic_meta[0]
    topic_type = topic_meta[1]
    mon_man = topic_meta[2]
    global MODE_MANAGER_LIST

    if topic_type == LaserScan:
        # remove infinite ranges
        cleaned_ranges = [value for value in data.ranges if value < float('inf')]
        data_msg = min(cleaned_ranges)
        mon_man.message_broker.forward_msg(topic_str, data_msg)
        # wait pub_time_wait
        # time.sleep(mon_man.topic_list[topic_str])
        time.sleep(MODE_MANAGER_LIST[topic_str[1:6]].fq)


def on_trigger(client, userdata, message):
    global MODE_MANAGER_LIST, REGISTRY
    raw_msg_data = message.payload.decode("utf-8")
    data_obj = json.loads(raw_msg_data, object_hook=lambda d: SimpleNamespace(**d))

    new_mode = data_obj.mode
    device_name_to_be_switched = data_obj.device

    safety_critical_zone = ""
    for device in REGISTRY.device_list:
        if device.name == device_name_to_be_switched:
            safety_critical_zone = device.zone_id

    if new_mode == "maintenance":
        for key, single_mode_m in MODE_MANAGER_LIST.items():
            # switch into maintenance mode
            if key == device_name_to_be_switched:
                single_mode_m.startMaintenance()
            else:
                # switch into precautious modes
                for device in REGISTRY.device_list:
                    if device.name == key:
                        #  ---> if it can move freely
                        for single_property in device.property_list:
                            if single_property.property_name == "can_move_freely" and single_property.is_active:
                                single_mode_m.startSafeMode()
                        #  ---> or is in the same zone
                        if safety_critical_zone and device.zone_id == safety_critical_zone:
                            single_mode_m.startSafeMode()

            rospy.loginfo(f"current mode for {key} >>> {single_mode_m.current_state}")


class MonitoringManager(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MonitoringManager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__()
        rospy.init_node('pre_mon', anonymous=True)
        self.topic_list = {}
        self.message_broker = MessageBroker()

    def update_topic(self, topic_name: str, init_pub_time_wait: float) -> None:
        """Adds a topic to the topic list"""

        if isinstance(topic_name, str) and isinstance(init_pub_time_wait, float):
            if topic_name in self.topic_list:
                raise AttributeError(f"Topic already exists in topic_list: {topic_name}")
            else:
                self.topic_list[topic_name] = init_pub_time_wait
        else:
            raise ValueError("Couldn't  add topic as either topic_name is not a string or frequency is not a float!")

    def start_monitoring(self):
        """Creates a ROS node and subscribes to the topics"""

        # start dynamic subscriber
        for topic_name, pub_time_wait in self.topic_list.items():
            topic_type, topic_str, _ = rostopic.get_topic_class(topic_name)
            rospy.Subscriber(topic_str, topic_type, handle_new_mon_message,
                             [topic_str, topic_type, self])

        rospy.spin()

    # TODO: ship towards device once fully implemented
    def start_mode_listener(self, mode_manager, registry):
        global MODE_MANAGER_LIST, REGISTRY
        MODE_MANAGER_LIST = mode_manager
        REGISTRY = registry
        self.message_broker.subscribe_to_topic('trigger', on_trigger)
