from components.kafak_consumer import KafkaConsumer
from components.validation import Validation
from components.damage_config import DamageConfig
from shared.logger import log_event

kafka_consumer = KafkaConsumer(DamageConfig.get_bootstrap_servers(),'damage','damage_group',log_event)
validation = Validation()


while True:
    data = kafka_consumer.consume()
    new_data = validation.full_inspection(data)
    if new_data[0]:
        print(new_data)


