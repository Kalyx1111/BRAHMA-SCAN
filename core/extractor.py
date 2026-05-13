import os
import zipfile
import shutil
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_tools")

LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(EXTRACTED_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "extractor.log")


# ==========================================
# LOGGING
# ==========================================
def write_log(message):

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")

    print(message)


# ==========================================
# EXTRACT ZIP
# ==========================================
def extract_zip(zip_path):

    try:

        zip_name = os.path.splitext(os.path.basename(zip_path))[0]

        extract_path = os.path.join(EXTRACTED_DIR, zip_name)

        if os.path.exists(extract_path):

            write_log(f"ALREADY EXISTS -> {zip_name}")

            return

        os.makedirs(extract_path, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        write_log(f"EXTRACTED -> {zip_name}")

    except Exception as e:

        write_log(f"ERROR -> {zip_path} -> {str(e)}")


# ==========================================
# SCAN DOWNLOADS
# ==========================================
def scan_downloads():

    write_log("SCANNING DOWNLOADS FOLDER")

    files = os.listdir(DOWNLOADS_DIR)

    zip_files = [f for f in files if f.lower().endswith(".zip")]

    if not zip_files:

        write_log("NO ZIP FILES FOUND")
        return

    for file in zip_files:

        zip_path = os.path.join(DOWNLOADS_DIR, file)

        extract_zip(zip_path)


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    scan_downloads()