import pytest
from inventory_service.services.commands import ReserveItemCommand
from inventory_service.domain.models import InventoryLog
from shared.kafka_producer import publish
from shared.kafka_consumer import get_consumer
import threading
import time

class FakeInventoryRepo:
    def __init__(self):
        self.saved = None

    def save(self, log: InventoryLog):
        self.saved = log

def test_reserve_item():
    repo = FakeInventoryRepo()
    cmd = ReserveItemCommand(repo)
    cmd.execute("ORD-321", ["itemA"])
    assert repo.saved.order_id == "ORD-321"
    assert repo.saved.items == ["itemA"]

@pytest.mark.kafka
def test_item_reserved_event():
    received = {}

    def listen():
        consumer = get_consumer("item_reserved")
        for msg in consumer:
            if msg.value['order_id'] == "ORD-KAFKA-INV":
                received.update(msg.value)
                break

    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

    repo = FakeInventoryRepo()
    cmd = ReserveItemCommand(repo)
    cmd.execute("ORD-KAFKA-INV", ["X"])
    time.sleep(2)
    assert received.get("order_id") == "ORD-KAFKA-INV"
    