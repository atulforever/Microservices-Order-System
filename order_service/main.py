# order_service/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from order_service.services.commands import CreateOrderCommand
from order_service.adapters.repository import OrderRepository

app = FastAPI()
repo = OrderRepository()
create_order = CreateOrderCommand(repo)

class OrderRequest(BaseModel):
    order_id: str
    items: list[str]

@app.post("/orders")
def place_order(req: OrderRequest):
    create_order.execute(req.order_id, req.items)
    return {"status": "Order Placed"}
