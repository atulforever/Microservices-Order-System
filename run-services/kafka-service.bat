SET KAFKA_HOME=D:\kafka_2.12-3.9.1
SET KAFKA_CONFIG=%KAFKA_HOME%\config\server.properties
cd /d %KAFKA_HOME%
%KAFKA_HOME%\bin\windows\kafka-server-start.bat %KAFKA_CONFIG%
