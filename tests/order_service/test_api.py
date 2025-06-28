from fastapi.testclient import TestClient
from order_service.main import app

client = TestClient(app)

def test_create_order_api():
    response = client.post("/orders", json={"order_id": "ORD-999", "items": ["itemX"]})
    assert response.status_code == 200
    assert response.json()["status"] == "Order Placed"
