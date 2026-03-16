from components.kafak_consumer import KafkaConsumer
from components.validation import Validation
from components.attack_config import AttackConfig
from shared.logger import log_event
from db.main import push_to_db


kafka_consumer = KafkaConsumer(AttackConfig.get_bootstrap_servers(),'attack','attack_group',log_event)
validation = Validation()


while True:
    data = kafka_consumer.consume()
    data_stor = validation.full_inspection(data)
    if data_stor[0]:
        push_to_db.insert_into_attack(data_stor[1])



