# 🛡️ File Scanner Tool – Python GUI-Based Security Utility

A beginner-friendly yet powerful GUI-based **File Scanner Tool** built with Python. It scans any file locally for potentially malicious patterns and behaviors, offering a security verdict along with a detailed **PDF report** generation using the `reportlab` library.

> 🔗 **Repository**: [github.com/RupeshVerma28/Simple-File-Scanner-](https://github.com/RupeshVerma28/Simple-File-Scanner-.git)

---

## 📌 Overview

This tool is designed for:
- 🔰 Beginners learning Cybersecurity and Python
- 🔐 Basic security analysis of suspicious files
- 🧾 Easy report generation and file assessment

The tool operates **completely offline** with no third-party API dependencies, making it lightweight, fast, and privacy-safe.

---

## 🖥️ Features

| Feature                        | Description |
|-------------------------------|-------------|
| ✅ **Local File Scanning**      | Scan any file on your system for threats |
| 🔍 **Suspicious Code Detection** | Detects usage of `eval()`, `exec()`, `os.system()`, etc. |
| 🧠 **Heuristic Analysis**       | Flags `.exe`, `.bat`, `.vbs`, `.py` scripts, and encoded content |
| 🔐 **SHA-256 Hashing**         | Securely generate the hash of the file |
| 📄 **PDF Report Generation**   | Export a clean, readable security report with scan results |
| 🎨 **Modern GUI with CustomTkinter** | Dark-themed and responsive user interface |

---

## 🔧 Technologies Used

- **Python 3.8+**
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) – for GUI
- [`reportlab`](https://www.reportlab.com/dev/install/opensource/) – for PDF generation
- `os`, `hashlib`, and standard libraries for file scanning

---

## 📂 Folder Structure
Simple-File-Scanner-/
├── file_scanner_tool.py        # Main scanner script
├── scan_report.pdf             # Output report file
├── README.md                   # Documentation
└── assets/
    └── screenshot.png          # GUI preview (optional)


