# Microservices Order System (Python + Kafka + MySQL)

This project is a demonstration of a microservices-based architecture using Python, FastAPI, Kafka, and MySQL. It simulates an **order booking system** with inventory and shipping services that communicate through **event-driven architecture**.

---

## 🧩 Architecture Overview

- **Order Service**: Accepts order requests and emits `item_ordered` events.
- **Inventory Service**: Listens to `item_ordered`, reserves items, and emits `item_reserved` events.
- **Shipping Service**: Listens to `item_reserved`, schedules delivery, and emits `shipping_scheduled` events.
- **Shared**: Contains Kafka producers/consumers, DB connectors, and event schemas.
- **API Gateway**: Forwards API calls to underlying services.

---

## 📦 Tech Stack

- **Python 3.13+**
- **FastAPI**
- **Kafka (via Docker)**
- **MySQL 8+**
- **Kafka Python client (`kafka-python`)**
- **MySQL Connector (`mysql-connector-python`)**
- **HTTPX**

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/atulforever/Microservices-Order-System.git
cd Microservices-Order-System
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start Kafka & MySQL
```bash
docker-compose up -d
```

### 4. Set up Database
Run the following SQL script in your MySQL server:
```sql
CREATE DATABASE microservice_db;
USE microservice_db;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(100),
    items TEXT
);

CREATE TABLE inventory_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(100),
    items_reserved TEXT
);

CREATE TABLE shipping_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(100),
    status VARCHAR(50)
);
```

### 5. Run Services
```bash
# Order API
uvicorn order_service.main:app --port 8000

# Inventory Kafka Consumer
set PYTHONPATH=.
python inventory_service/consumer.py

# Shipping Kafka Consumer
set PYTHONPATH=.
python shipping_service/consumer.py

# API Gateway
uvicorn api_gateway.main:app --port 9000
```

### 6. Test the Flow
```bash
curl -X POST http://localhost:9000/api/orders \
  -H "Content-Type: application/json" \
  -d '{"order_id": "ORD101", "items": ["itemA", "itemB"]}'
```

---

## 🧪 Running Tests

### Unit + Kafka Event Tests
```bash
pytest tests/
```

You can run only Kafka-based tests using:
```bash
pytest -m kafka
```

---

## 📂 Directory Structure
```
.
├── shared/
├── order_service/
├── inventory_service/
├── shipping_service/
├── api_gateway/
├── tests/
└── docker-compose.yml
```

---

## 🔒 Security & Extensions
- Add JWT auth in the API Gateway
- Add Prometheus + Grafana metrics
- Add service health checks and retries

---

## 📄 License
MIT
