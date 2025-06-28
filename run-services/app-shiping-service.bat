@echo off
REM Starting Shipping Service...
cd /d D:\node\python\services
call .venv\Scripts\activate
set PYTHONPATH=.
python ./shipping_service/consumer.py


