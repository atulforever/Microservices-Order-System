@echo off
REM Starting Order Service...
cd /d D:\node\python\services
call .venv\Scripts\activate
set PYTHONPATH=.
uvicorn order_service.main:app --reload --port 8000



