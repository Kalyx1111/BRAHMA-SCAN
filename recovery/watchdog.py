import subprocess
import requests
import time
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORE_DIR = os.path.join(BASE_DIR, "core")

LOG_DIR = os.path.join(BASE_DIR, "logs")

SERVER_FILE = os.path.join(CORE_DIR, "server.py")

os.makedirs(LOG_DIR, exist_ok=True)

WATCHDOG_LOG = os.path.join(LOG_DIR, "watchdog.log")

SERVER_URL = "http://127.0.0.1:5000"


# ==========================================
# LOGGING
# ==========================================
def write_log(message):

    with open(WATCHDOG_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")

    print(message)


# ==========================================
# CHECK SERVER
# ==========================================
def is_server_running():

    try:
        requests.get(SERVER_URL, timeout=5)
        return True

    except:
        return False


# ==========================================
# START SERVER
# ==========================================
def start_server():

    write_log("SERVER DOWN -> STARTING SERVER")

    subprocess.Popen(
        ["python", SERVER_FILE],
        cwd=CORE_DIR
    )

    time.sleep(5)


# ==========================================
# WATCHDOG LOOP
# ==========================================
def watchdog_loop():

    write_log("WATCHDOG STARTED")

    while True:

        if not is_server_running():

            write_log("SERVER NOT RESPONDING")

            start_server()

        else:

            write_log("SERVER RUNNING OK")

        time.sleep(15)


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    watchdog_loop()