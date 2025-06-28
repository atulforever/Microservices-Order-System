# inventory_service/adapters/repository.py
from shared.db import get_connection
from inventory_service.domain.models import InventoryLog

class InventoryRepository:
    def save(self, log: InventoryLog):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO inventory_logs (order_id, items_reserved) VALUES (%s, %s)",
            (log.order_id, ",".join(log.items))
        )
        conn.commit()
        cursor.close()
        conn.close()