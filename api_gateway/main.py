from fastapi import FastAPI, Request
import httpx

app = FastAPI()

ORDER_SERVICE_URL = "http://localhost:8000/orders"

@app.post("/api/orders")
async def create_order(request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(ORDER_SERVICE_URL, json=payload)
    return response.json()