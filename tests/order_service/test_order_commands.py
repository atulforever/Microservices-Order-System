import pytest
from order_service.services.commands import CreateOrderCommand
from order_service.domain.models import Order
from shared.events import ItemOrdered
from shared.kafka_producer import publish
from shared.kafka_consumer import get_consumer
import threading
import time

class FakeOrderRepo:
    def __init__(self):
        self.saved = None

    def save(self, order: Order):
        self.saved = order

@pytest.fixture
def order_repo():
    return FakeOrderRepo()

def test_create_order_command(order_repo):
    command = CreateOrderCommand(order_repo)
    command.execute("ORD-123", ["item1", "item2"])
    assert order_repo.saved.order_id == "ORD-123"
    assert order_repo.saved.items == ["item1", "item2"]

# Kafka event verification
@pytest.mark.kafka
def test_kafka_event_published():
    received = {}

    def listen():
        consumer = get_consumer("item_ordered")
        for msg in consumer:
            if msg.value['order_id'] == "ORD-KAFKA-001":
                received.update(msg.value)
                break

    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

    publish("item_ordered", ItemOrdered("ORD-KAFKA-001", ["itemX"]))
    time.sleep(2)
    assert received.get("order_id") == "ORD-KAFKA-001"
    