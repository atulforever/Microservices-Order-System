# shared/events.py
from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class ItemOrdered(Event):
    def __init__(self, order_id: str, items: list[str]):
        self.order_id = order_id
        self.items = items

    def to_dict(self):
        return {"order_id": self.order_id, "items": self.items}

class ItemReserved(Event):
    def __init__(self, order_id: str):
        self.order_id = order_id

    def to_dict(self):
        return {"order_id": self.order_id}

class ShippingScheduled(Event):
    def __init__(self, order_id: str):
        self.order_id = order_id

    def to_dict(self):
        return {"order_id": self.order_id}