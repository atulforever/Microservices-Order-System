# order_service/adapters/repository.py
from shared.db import get_connection
from order_service.domain.models import Order

class OrderRepository:
    def save(self, order: Order):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (order_id, items) VALUES (%s, %s)",
            (order.order_id, ",".join(order.items))
        )
        conn.commit()
        cursor.close()
        conn.close()