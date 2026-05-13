@echo off

cd /d %~dp0

cd ..

python core\server.py

pause