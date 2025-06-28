# shipping_service/consumer.py
from shared.kafka_consumer import get_consumer
from shipping_service.adapters.repository import ShippingRepository
from shipping_service.services.commands import ScheduleShippingCommand

consumer = get_consumer("item_reserved")
repo = ShippingRepository()
schedule_command = ScheduleShippingCommand(repo)
print("[Shipping] Listening for 'item_reserved' events...")

for msg in consumer:
    data = msg.value
    schedule_command.execute(data['order_id'])
    print(f"[Shipping] Scheduled shipment for Order {data['order_id']}")