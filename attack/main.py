from components.kafak_consumer import KafkaConsumer
from components.validation import Validation


kafka_consumer = KafkaConsumer('localhost:9092','damage','damage_group','a')
validation = Validation()


while True:
    data = kafka_consumer.consume()
    new_data = validation.full_inspection(data)
    if new_data[0]:
        print(new_data)


