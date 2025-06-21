# 💠 INITIUM

![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat&logo=python)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-green?style=flat&logo=windows)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> **Initium** *(Latin: "permulaan")* adalah sebuah CLI interaktif untuk menginstal berbagai tools pemrograman web seperti Node.js, VSCode, Git, Python, XAMPP, dan Laragon secara otomatis, cukup sekali jalan, multi-OS.

---

## 🚀 Fitur

- ⚡ Instalasi cepat dan otomatis
- 🖥️ Kompatibel: macOS, Linux, dan Windows
- 🎨 UI CLI yang menarik dengan `rich` + `pyfiglet`
- 🤖 Deteksi sistem operasi secara otomatis
- 🔧 Struktur modular, mudah dikembangkan

---

## 🧪 Tools yang Didukung

| Tool       | macOS | Linux | Windows |
|------------|:-----:|:-----:|:-------:|
| Node.js    | ✅     | ✅     | ✅       |
| VSCode     | ✅     | ✅     | ✅       |
| Git        | ✅     | ✅     | ✅       |
| Python     | ✅     | ✅     | ✅       |
| XAMPP      | 🌐    | 🌐    | 🌐      |
| Laragon    | ❌     | ❌     | ✅       |

---

## 📦 Requirement macOS 13 or later
Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
---

## 📦 Instalasi

```bash
git clone https://github.com/namamu/initium.git
cd initium


## 🛠 Setup Virtual Environment

python3 -m venv .venv
source .venv/bin/activate     # macOS/Linux
# .venv\Scripts\activate.bat  # Windows

## 📦 Install Dependensi
pip install -r requirement.txt # Windows
pip3 install -r requirement.txt # macOS/Linux

▶️ Menjalankan Program

💡 Opsi 1: Manual
python initium/main.py

💡 Opsi 2: Auto cross-platform (rekomendasi)
python run.py
```
---
# Initium - Web Dev Setup CLI 🚀

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Initium is a simple cross-platform CLI tool that helps you quickly install essential web development tools like Node.js, Git, Python, VSCode, XAMPP, and Laragon.

...

## 📝 License

This project is licensed under the [MIT License](LICENSE.md).
