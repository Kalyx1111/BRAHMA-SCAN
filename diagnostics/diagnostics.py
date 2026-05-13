import os
import platform
import socket
import shutil
import psutil
import requests
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

REPORT_FILE = os.path.join(LOG_DIR, "diagnostics_report.txt")


# ==========================================
# INTERNET CHECK
# ==========================================
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return "CONNECTED"
    except:
        return "NO INTERNET"


# ==========================================
# SYSTEM INFO
# ==========================================
def get_system_info():

    total, used, free = shutil.disk_usage("/")

    ram = psutil.virtual_memory()

    info = {
        "TIME": str(datetime.now()),
        "OS": platform.system(),
        "OS_VERSION": platform.version(),
        "MACHINE": platform.machine(),
        "PROCESSOR": platform.processor(),
        "PYTHON_VERSION": platform.python_version(),
        "HOSTNAME": socket.gethostname(),
        "RAM_TOTAL_GB": round(ram.total / (1024 ** 3), 2),
        "RAM_AVAILABLE_GB": round(ram.available / (1024 ** 3), 2),
        "DISK_TOTAL_GB": round(total / (1024 ** 3), 2),
        "DISK_FREE_GB": round(free / (1024 ** 3), 2),
        "INTERNET": check_internet()
    }

    return info


# ==========================================
# SAVE REPORT
# ==========================================
def save_report(data):

    with open(REPORT_FILE, "w", encoding="utf-8") as f:

        f.write("=" * 50 + "\n")
        f.write("BRAHMA SCAN FULL DIAGNOSTICS REPORT\n")
        f.write("=" * 50 + "\n\n")

        for key, value in data.items():
            line = f"{key}: {value}"
            print(line)
            f.write(line + "\n")

    print("\nDiagnostics report saved.")
    print(REPORT_FILE)


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    data = get_system_info()

    save_report(data)