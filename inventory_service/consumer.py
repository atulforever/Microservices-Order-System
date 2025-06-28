# inventory_service/consumer.py
from shared.kafka_consumer import get_consumer
from inventory_service.adapters.repository import InventoryRepository
from inventory_service.services.commands import ReserveItemCommand

consumer = get_consumer("item_ordered")
repo = InventoryRepository()
reserve_command = ReserveItemCommand(repo)
print("[Inventory] Listening for 'item_ordered' events...")

for msg in consumer:
    data = msg.value
    reserve_command.execute(data['order_id'], data['items'])
    print(f"[Inventory] Reserved items for Order {data['order_id']}")