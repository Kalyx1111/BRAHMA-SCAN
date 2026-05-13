# BRAHMA SCAN FULL

BRAHMA SCAN FULL is a lightweight web-based OSINT and reconnaissance platform built for cybersecurity researchers, bug bounty hunters, investigators, students, and security professionals.

The project combines multiple reconnaissance workflows into a single browser-based interface while using a Python Flask backend for execution and management.

Look for "brahma_scan_lite" inside "BRAHMA_SCAN_FULL" folder to run lite version or 
Look for "START_BRAHMA_FULL.bat" inside "launchers" sub folder of "BRAHMA_SCAN_FULL" folder.

---

# FEATURES

- Web-based OSINT interface
- Python Flask backend
- Cross-platform support
- Responsive browser frontend
- Local execution of reconnaissance tools
- Single-user local deployment
- Browser-based operation
- Mobile browser support
- LAN accessibility
- GitHub-friendly project structure

---

# INCLUDED TOOLS

Currently integrated tools:

- Subfinder
- Amass
- Katana

These tools are executed locally from the backend.

---

# PROJECT STRUCTURE

```plaintext
BRAHMA_SCAN_FULL
│
├── core
│   ├── server.py
│   └── tool_runner.py
│
├── web
│   └── index.html
│
├── extracted_tools
│   ├── subfinder
│   ├── amass
│   └── katana
│
├── launchers
│   └── START_BRAHMA_FULL.bat (Double click this file to run it)
│
├── logs
│
├── reports
│
├── requirements.txt
│
└── README.md
│
└── brahma_scan_lite (you can also use this lite version)
```

---

# REQUIREMENTS

Before running BRAHMA SCAN FULL install:

- Python 3.10 or higher
- pip
- Modern browser:
  - Chrome
  - Edge
  - Firefox
  - Brave

---

# INSTALLATION

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

OR download ZIP from GitHub.

---

## 2. Open Project Folder

```bash
cd BRAHMA_SCAN_FULL
```

---

## 3. Install Python Requirements

```bash
pip install -r requirements.txt
```

---

# RUNNING THE PROJECT

## Windows

Double click:

```plaintext
launchers/START_BRAHMA_FULL.bat
```

OR:

```bash
python core/server.py
```

---

# ACCESSING THE PANEL

Open browser:

```plaintext
http://127.0.0.1:5000
```

---

# MOBILE ACCESS

Devices connected on the same WiFi network can access:

```plaintext
http://YOUR_LOCAL_IP:5000
```

Example:

```plaintext
http://192.168.1.9:5000
```

---

# IMPORTANT NOTES

- This project is intended for educational and authorized security research only.
- Do not use against systems without permission.
- User is responsible for complying with local laws and regulations.

---

# AI SUPPORT

BRAHMA SCAN FULL is designed for online AI integrations using APIs such as:

- OpenAI
- Gemini
- Claude
- DeepSeek

No offline AI or local LLM setup is required.
You can create offline setup also if you want for analysis locally.

---

# SUPPORTED OPERATING SYSTEMS

- Windows
- Linux
- macOS

The frontend also works on:

- Android browsers
- iPhone browsers
- Tablets

---

# TROUBLESHOOTING

## Flask Not Starting

Install Flask:

```bash
pip install flask
```

---

## Port Already In Use

Close previous Python/Flask instances or change port inside:

```plaintext
core/server.py
```

---

## Browser Does Not Open

Manually visit:

```plaintext
http://127.0.0.1:5000
```

---

# DISCLAIMER

This software is provided for educational and research purposes only.

The developer is not responsible for misuse, illegal activity, or damages caused by this project.

---

# AUTHOR

BRAHMA SCAN FULL