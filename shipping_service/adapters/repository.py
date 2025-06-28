# shipping_service/adapters/repository.py
from shared.db import get_connection
from shipping_service.domain.models import ShippingLog

class ShippingRepository:
    def save(self, log: ShippingLog):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO shipping_logs (order_id, status) VALUES (%s, %s)",
            (log.order_id, log.status)
        )
        conn.commit()
        cursor.close()
        conn.close()