import pytest
from shipping_service.services.commands import ScheduleShippingCommand
from shipping_service.domain.models import ShippingLog
from shared.kafka_producer import publish
from shared.kafka_consumer import get_consumer
import threading
import time

class FakeShippingRepo:
    def __init__(self):
        self.saved = None

    def save(self, log: ShippingLog):
        self.saved = log

def test_schedule_shipping():
    repo = FakeShippingRepo()
    cmd = ScheduleShippingCommand(repo)
    cmd.execute("ORD-654")
    assert repo.saved.order_id == "ORD-654"
    assert repo.saved.status == "Scheduled"

@pytest.mark.kafka
def test_shipping_scheduled_event():
    received = {}

    def listen():
        consumer = get_consumer("shipping_scheduled")
        for msg in consumer:
            if msg.value['order_id'] == "ORD-KAFKA-SHIP":
                received.update(msg.value)
                break

    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

    repo = FakeShippingRepo()
    cmd = ScheduleShippingCommand(repo)
    cmd.execute("ORD-KAFKA-SHIP")
    time.sleep(2)
    assert received.get("order_id") == "ORD-KAFKA-SHIP"
