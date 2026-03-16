from confluent_kafka import Producer
import json

class KafkaProducer:
    def __init__(self, bootstrap_servers, topic_name, logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_name
        self.logger = logger
        self.producer_config = {
            "bootstrap.servers": self.bootstrap_servers
        }
        self.producer = Producer(self.producer_config)

    def send(self,event):
        value = json.dumps(event).encode("utf-8")

        self.producer.produce(
            topic="orders",
            value=value,
            callback=self.delivery_report
        )

        self.producer.flush()
        self.logger('INFO', f'i send new msg to topic: {self.topic_name}')

    @staticmethod
    def delivery_report(self,err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered {msg.value().decode("utf-8")}")
            print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")








