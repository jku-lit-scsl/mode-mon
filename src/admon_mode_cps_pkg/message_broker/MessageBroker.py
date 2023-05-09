import sys

from admon_mode_cps_pkg.util.util import generate_uuid
import paho.mqtt.client as mqtt


class MessageBroker(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessageBroker, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__()
        self.client = mqtt.Client(f"{generate_uuid()}-mqttclient")
        self.client.connect('localhost')

    def forward_msg(self, topic_str, msg):
        self.client.publish(topic_str[1:], msg)
