# shipping_service/domain/models.py
class ShippingLog:
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status