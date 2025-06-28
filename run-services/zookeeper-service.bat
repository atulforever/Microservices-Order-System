@echo off
SET ZOOKEEPER_HOME=D:\kafka_2.12-3.9.1
SET ZOOKEEPER_CONFIG=%ZOOKEEPER_HOME%\config\zookeeper.properties
cd /d %ZOOKEEPER_HOME%
%ZOOKEEPER_HOME%\bin\windows\zookeeper-server-start.bat %ZOOKEEPER_CONFIG%
