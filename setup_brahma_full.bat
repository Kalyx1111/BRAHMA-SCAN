@echo off
setlocal EnableDelayedExpansion
color 0A
mode con: cols=110 lines=35

cd /d C:\BRAHMA_SCAN_FULL

echo.
echo ================================================================
echo                BRAHMA SCAN FULL - CORE INSTALLER
echo ================================================================
echo.

timeout /t 1 >nul

:: ================================================================
:: CHECK PYTHON
:: ================================================================

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found.
    echo.
    echo Install Python 3.11+ from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b
)

echo [OK] Python detected.

:: ================================================================
:: CREATE FOLDERS
:: ================================================================

echo.
echo [INFO] Creating BRAHMA_SCAN_FULL structure...

mkdir core 2>nul
mkdir modules 2>nul
mkdir assets 2>nul
mkdir tools 2>nul
mkdir ai 2>nul
mkdir ai\providers 2>nul
mkdir ai\cache 2>nul
mkdir ai\local 2>nul
mkdir ghdb 2>nul
mkdir cache 2>nul
mkdir cache\queries 2>nul
mkdir cache\ai 2>nul
mkdir cache\temp 2>nul
mkdir logs 2>nul
mkdir recovery 2>nul
mkdir recovery\crash_logs 2>nul
mkdir diagnostics 2>nul
mkdir launchers 2>nul
mkdir web 2>nul
mkdir web\css 2>nul
mkdir web\js 2>nul
mkdir web\assets 2>nul
mkdir mobile 2>nul
mkdir mobile\pwa 2>nul
mkdir mobile\apk 2>nul
mkdir database 2>nul
mkdir extracted_tools 2>nul
mkdir downloads 2>nul

:: ================================================================
:: COPY HTML INTO WEB
:: ================================================================

if exist brahma_scan_lite.html (
    copy /Y brahma_scan_lite.html web\index.html >nul
    echo [OK] HTML copied to web\index.html
) else (
    echo [WARN] brahma_scan_lite.html not found.
)

:: ================================================================
:: CREATE CONFIG
:: ================================================================

echo.
echo [INFO] Creating config files...

(
echo {
 echo   "version":"1.0",
 echo   "mode":"FULL",
 echo   "auto_browser":true,
 echo   "diagnostics":true,
 echo   "recovery":true,
 echo   "local_ai_optional":true,
 echo   "default_port":8080
 echo }
) > core\config.json

:: ================================================================
:: CREATE GHDB DATABASE PLACEHOLDERS
:: ================================================================

(
echo []
) > ghdb\dorks.json

(
echo []
) > ghdb\operators.json

(
echo []
) > ghdb\cves.json

:: ================================================================
:: CREATE PYTHON REQUIREMENTS
:: ================================================================

(
echo flask
 echo flask-cors
 echo requests
 echo psutil
 echo colorama
) > requirements.txt

:: ================================================================
:: INSTALL PYTHON PACKAGES
:: ================================================================

echo.
echo [INFO] Installing Python packages...

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

:: ================================================================
:: CREATE MAIN PYTHON LAUNCHER
:: ================================================================

echo.
echo [INFO] Creating launcher.py ...

(
echo import os
 echo import sys
 echo import json
 echo import time
 echo import socket
 echo import webbrowser
 echo import platform
 echo import threading
 echo from flask import Flask, send_from_directory
 echo.
 echo BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 echo WEB_DIR = os.path.join(BASE_DIR, 'web')
 echo LOG_DIR = os.path.join(BASE_DIR, 'logs')
 echo.
 echo app = Flask(__name__, static_folder=WEB_DIR)
 echo.
 echo def log(msg):
 echo     print(f'[BRAHMA] {msg}')
 echo.
 echo def detect_os():
 echo     return platform.system()
 echo.
 echo def diagnostics():
 echo     log('Running diagnostics...')
 echo     log(f'OS: {detect_os()}')
 echo     log(f'Python: {sys.version}')
 echo.
 echo def watchdog():
 echo     while True:
 echo         time.sleep(30)
 echo         try:
 echo             with open(os.path.join(LOG_DIR, 'heartbeat.log'), 'a', encoding='utf-8') as f:
 echo                 f.write('heartbeat\\n')
 echo         except:
 echo             pass
 echo.
 echo @app.route('/')
 echo def index():
 echo     return send_from_directory(WEB_DIR, 'index.html')
 echo.
 echo @app.route('/^<path:path^>')
 echo def static_proxy(path):
 echo     return send_from_directory(WEB_DIR, path)
 echo.
 echo def get_port():
 echo     s = socket.socket()
 echo     s.bind(('',0))
 echo     port = s.getsockname()[1]
 echo     s.close()
 echo     return port
 echo.
 echo if __name__ == '__main__':
 echo     diagnostics()
 echo.
 echo     t = threading.Thread(target=watchdog, daemon=True)
 echo     t.start()
 echo.
 echo     port = 8080
 echo     url = f'http://127.0.0.1:{port}'
 echo.
 echo     log(f'Starting BRAHMA SCAN FULL on {url}')
 echo.
 echo     webbrowser.open(url)
 echo.
 echo     app.run(host='0.0.0.0', port=port, debug=False)
) > launcher.py

:: ================================================================
:: CREATE START FILE
:: ================================================================

(
echo @echo off
 echo cd /d C:\BRAHMA_SCAN_FULL
 echo python launcher.py
) > START_BRAHMA_FULL.bat

:: ================================================================
:: CREATE RECOVERY WATCHDOG
:: ================================================================

(
echo import os
 echo import time
 echo.
 echo while True:
 echo     time.sleep(60)
 echo     print('BRAHMA WATCHDOG ACTIVE')
) > recovery\watchdog.py

:: ================================================================
:: CREATE README
:: ================================================================

(
echo BRAHMA SCAN FULL
 echo.
 echo START:
 echo 1. Run START_BRAHMA_FULL.bat
 echo.
 echo FEATURES:
 echo - Local Python backend
 echo - Cross-platform structure
 echo - Diagnostics
 echo - Recovery watchdog
 echo - Browser auto-launch
 echo - Local databases
 echo - AI-ready architecture
) > README.txt

:: ================================================================
:: CREATE TOOL DOWNLOAD PLACEHOLDERS
:: ================================================================

mkdir tools\spiderfoot 2>nul
mkdir tools\photon 2>nul
mkdir tools\theharvester 2>nul
mkdir tools\subfinder 2>nul
mkdir tools\katana 2>nul
mkdir tools\nuclei 2>nul

:: ================================================================
:: COMPLETE
:: ================================================================

echo.
echo ================================================================
echo               BRAHMA SCAN FULL INSTALLED
echo ================================================================
echo.
echo ROOT: C:\BRAHMA_SCAN_FULL

echo.
echo NEXT:
echo 1. Put your FULL HTML into:
echo    web\index.html

echo 2. Run:
echo    START_BRAHMA_FULL.bat

echo.
echo DONE.
echo.
pause