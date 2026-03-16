from components.kafak_consumer import KafkaConsumer
from components.kafka_producer import KafkaProducer
from components.intel_config import IntelConfig
from components.validation import Validation
from shared.logger import log_event



kafka_consumer = KafkaConsumer(IntelConfig.get_bootstrap_servers(),'intel','intel_group',log_event)
kafka_producer = KafkaProducer(IntelConfig.get_bootstrap_servers(),'intel_signals_dlq',log_event)
validation = Validation()


while True:
    data = kafka_consumer.consume()
    data_send = validation.full_inspection(data)
    if not data_send[0]:
        kafka_producer.send(data_send[1] + '-' + data )






