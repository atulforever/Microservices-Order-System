# inventory_service/domain/models.py
class InventoryLog:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items