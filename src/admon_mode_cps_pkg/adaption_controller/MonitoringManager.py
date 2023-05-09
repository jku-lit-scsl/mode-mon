import time

import rospy
import rostopic
from admon_mode_cps_pkg.message_broker.MessageBroker import MessageBroker
from sensor_msgs.msg import LaserScan


def handle_new_mon_message(data, topic_meta):
    topic_str = topic_meta[0]
    topic_type = topic_meta[1]
    mon_man = topic_meta[2]

    if topic_type == LaserScan:
        # remove infinite ranges
        cleaned_ranges = [value for value in data.ranges if value < float('inf')]
        data_msg = min(cleaned_ranges)
        mon_man.message_broker.forward_msg(topic_str, data_msg)
        # wait pub_time_wait
        time.sleep(mon_man.topic_list[topic_str])


class MonitoringManager(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MonitoringManager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__()
        self.topic_list = {}
        self.message_broker = MessageBroker()

    def add_topic(self, topic_name: str, init_pub_time_wait: float) -> None:
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
        rospy.init_node('pre_mon', anonymous=True)

        # start dynamic subscriber
        for topic_name, pub_time_wait in self.topic_list.items():
            topic_type, topic_str, _ = rostopic.get_topic_class(topic_name)
            rospy.Subscriber(topic_str, topic_type, handle_new_mon_message,
                             [topic_str, topic_type, self])

        rospy.spin()
