# shared/kafka_consumer.py
from kafka import KafkaConsumer
import json

def get_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=f'{topic}_group'
    )