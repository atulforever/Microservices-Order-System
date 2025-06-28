# inventory_service/services/commands.py
from inventory_service.domain.models import InventoryLog
from inventory_service.adapters.repository import InventoryRepository
from shared.events import ItemReserved
from shared.kafka_producer import publish

class ReserveItemCommand:
    def __init__(self, repo: InventoryRepository):
        self.repo = repo

    def execute(self, order_id: str, items: list[str]):
        log = InventoryLog(order_id, items)
        self.repo.save(log)
        publish("item_reserved", ItemReserved(order_id))
