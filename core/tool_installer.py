import os
import platform
import zipfile
import shutil
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
EXTRACT_DIR = os.path.join(BASE_DIR, "extracted_tools")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

SYSTEM = platform.system().lower()

TOOLS = {}

# =========================
# WINDOWS
# =========================
if "windows" in SYSTEM:

    TOOLS = {
        "subfinder": {
            "url": "https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder_2.6.6_windows_amd64.zip",
            "zip": "subfinder.zip",
            "extract_folder": "subfinder"
        },

        "amass": {
            "url": "https://github.com/owasp-amass/amass/releases/latest/download/amass_windows_amd64.zip",
            "zip": "amass.zip",
            "extract_folder": "amass"
        },

        "katana": {
            "url": "https://github.com/projectdiscovery/katana/releases/latest/download/katana_1.1.0_windows_amd64.zip",
            "zip": "katana.zip",
            "extract_folder": "katana"
        }
    }

# =========================
# LINUX
# =========================
elif "linux" in SYSTEM:

    TOOLS = {
        "subfinder": {
            "url": "https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder_2.6.6_linux_amd64.zip",
            "zip": "subfinder.zip",
            "extract_folder": "subfinder"
        },

        "amass": {
            "url": "https://github.com/owasp-amass/amass/releases/latest/download/amass_linux_amd64.zip",
            "zip": "amass.zip",
            "extract_folder": "amass"
        },

        "katana": {
            "url": "https://github.com/projectdiscovery/katana/releases/latest/download/katana_1.1.0_linux_amd64.zip",
            "zip": "katana.zip",
            "extract_folder": "katana"
        }
    }

# =========================
# MAC
# =========================
elif "darwin" in SYSTEM:

    TOOLS = {
        "subfinder": {
            "url": "https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder_2.6.6_macOS_amd64.zip",
            "zip": "subfinder.zip",
            "extract_folder": "subfinder"
        },

        "amass": {
            "url": "https://github.com/owasp-amass/amass/releases/latest/download/amass_darwin_amd64.zip",
            "zip": "amass.zip",
            "extract_folder": "amass"
        },

        "katana": {
            "url": "https://github.com/projectdiscovery/katana/releases/latest/download/katana_1.1.0_macOS_amd64.zip",
            "zip": "katana.zip",
            "extract_folder": "katana"
        }
    }


def download_file(url, output_path):

    response = requests.get(url, stream=True)

    if response.status_code == 200:

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return True

    return False


def extract_zip(zip_path, extract_to):

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def install_tool(name, data):

    print(f"\n[+] Installing {name}")

    zip_path = os.path.join(DOWNLOAD_DIR, data["zip"])

    extract_path = os.path.join(EXTRACT_DIR, data["extract_folder"])

    if os.path.exists(extract_path):
        print(f"[✓] {name} already installed")
        return

    print("[+] Downloading...")

    success = download_file(data["url"], zip_path)

    if not success:
        print(f"[X] Failed downloading {name}")
        return

    print("[+] Extracting...")

    os.makedirs(extract_path, exist_ok=True)

    extract_zip(zip_path, extract_path)

    print(f"[✓] Installed {name}")


def main():

    print("\n===================================")
    print("BRAHMA SCAN TOOL INSTALLER")
    print("===================================")

    for tool_name, tool_data in TOOLS.items():
        install_tool(tool_name, tool_data)

    print("\n===================================")
    print("ALL TOOLS INSTALLED")
    print("===================================")


if __name__ == "__main__":
    main()