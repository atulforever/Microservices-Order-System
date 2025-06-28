# order_service/services/commands.py
from order_service.domain.models import Order
from order_service.adapters.repository import OrderRepository
from shared.events import ItemOrdered
from shared.kafka_producer import publish

class CreateOrderCommand:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str, items: list[str]):
        order = Order(order_id, items)
        self.repo.save(order)
        publish("item_ordered", ItemOrdered(order_id, items))