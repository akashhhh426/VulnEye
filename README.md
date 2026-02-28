# 🛡 VulnEye

VulnEye is a modular web security reconnaissance and analysis tool built in Python.

It performs passive security checks to identify common web misconfigurations and security weaknesses.

---

## 🚀 Features

- 🔐 Security Header Analysis
- 🍪 Cookie Security Inspection
- 🌐 CORS Misconfiguration Detection
- 🔑 Login Form Detection
- 🧠 JWT Token Analyzer
- 📊 Risk Scoring Engine
- ⚙ Modular Architecture

---

## 📦 Installation

```bash
git clone https://github.com/akashhhh426/VulnEye.git
cd VulnEye
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## ▶ Usage

Basic scan:

```bash
python3 vulneye.py https://example.com

Scan with JWT analysis:

python3 vulneye.py https://example.com --jwt YOUR_TOKEN


## ⚠ Disclaimer

VulnEye is intended for educational purposes and authorized security testing only.

Users are responsible for ensuring they have proper permission before scanning any website or system.  
The developer assumes no liability for misuse or damage caused by this tool.
