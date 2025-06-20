import os
import sys
import subprocess
import platform

def activate_and_run():
    system = platform.system()

    if system == "Windows":
        python_bin = ".venv\\Scripts\\python.exe"
    else:
        python_bin = "./.venv/bin/python"
    
    if not os.path.exists(python_bin):
        print("❌ Virtual environment tidak ditemukan. Silahkan jalankan")
        print(" python -m venv .venv")
        print(" lalu install requirements: ")
        print(" pip install -r requirements.txt")
        return

    # Jalankan main.py pakai python dari .venv
    subprocess.run([python_bin, "main.py"])

if __name__ == "__main__":
    activate_and_run()