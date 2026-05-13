import os
import subprocess
import platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOOLS_DIR = os.path.join(BASE_DIR, "extracted_tools")

WINDOWS = platform.system() == "Windows"


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300
        )

        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "code": result.returncode
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def get_subfinder_path():

    if WINDOWS:
        return os.path.join(
            TOOLS_DIR,
            "subfinder",
            "subfinder.exe"
        )

    return os.path.join(
        TOOLS_DIR,
        "subfinder",
        "subfinder"
    )


def get_amass_path():

    if WINDOWS:
        return os.path.join(
            TOOLS_DIR,
            "amass",
            "amass.exe"
        )

    return os.path.join(
        TOOLS_DIR,
        "amass",
        "amass"
    )


def get_katana_path():

    if WINDOWS:
        return os.path.join(
            TOOLS_DIR,
            "katana",
            "katana.exe"
        )

    return os.path.join(
        TOOLS_DIR,
        "katana",
        "katana"
    )


def run_subfinder(domain):

    tool = get_subfinder_path()

    command = f'"{tool}" -d {domain} -silent'

    return run_command(command)


def run_amass(domain):

    tool = get_amass_path()

    command = f'"{tool}" enum -passive -d {domain}'

    return run_command(command)


def run_katana(url):

    tool = get_katana_path()

    command = f'"{tool}" -u {url} -silent'

    return run_command(command)