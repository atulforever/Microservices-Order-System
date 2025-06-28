# shared/kafka_producer.py
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish(topic, event):
    if not hasattr(event, "to_dict"):
        raise TypeError(f"Event {event.__class__.__name__} must implement to_dict()")
    producer.send(topic, event.to_dict())
    producer.flush()