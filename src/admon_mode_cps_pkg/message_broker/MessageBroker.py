import paho.mqtt.client as mqtt
from admon_mode_cps_pkg.util.util import generate_uuid


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

    def subscribe_to_topic(self, topic, cb_on_message):
        self.client.subscribe(topic)
        self.client.on_message = cb_on_message
        self.client.loop_start()
