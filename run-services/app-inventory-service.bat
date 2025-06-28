@echo off
REM Starting Inventory Service...
cd /d D:\node\python\services
call .venv\Scripts\activate
set PYTHONPATH=.
python ./inventory_service/consumer.py


