# shipping_service/services/commands.py
from shipping_service.domain.models import ShippingLog
from shipping_service.adapters.repository import ShippingRepository
from shared.events import ShippingScheduled
from shared.kafka_producer import publish

class ScheduleShippingCommand:
    def __init__(self, repo: ShippingRepository):
        self.repo = repo

    def execute(self, order_id: str):
        log = ShippingLog(order_id, "Scheduled")
        self.repo.save(log)
        publish("shipping_scheduled", ShippingScheduled(order_id))