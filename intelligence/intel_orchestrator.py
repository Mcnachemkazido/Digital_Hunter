from components.kafak_consumer import KafkaConsumer
from components.kafka_producer import KafkaProducer
from components.intel_config import IntelConfig
from components.validation import Validation
from shared.logger import log_event


kafka_consumer = KafkaConsumer('localhost:9092','intel','intel_group',log_event)
kafka_producer = KafkaProducer('localhost:9092','intel_signals_dlq',log_event)
validation = Validation()


while True:
    data = kafka_consumer.consume()
    new_data = validation.full_inspection(data)
    if not new_data[0]:
        kafka_producer.send(new_data[1] + '-' + data )






