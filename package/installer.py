import subprocess
import os

def handle_choice(choice, os_type):
    tools = ["Node.js", "Visual Studio Code", "Git", "Python", "XAMPP", "Laragon"]

    try:
        choice = int(choice)
        if choice == 7:
            print("👋🏻 Keluar dari program!")
            return
        
        selected_tool = tools[choice - 1]
        print(f"🛠 Menginstall {selected_tool}...\n")

        if selected_tool == "Node.js":
            install_node(os_type)
        elif selected_tool == "Visual Studio Code":
            install_vscode(os_type)
        elif selected_tool == "Git":
            install_git(os_type)
        elif selected_tool == "Python":
            install_python(os_type)
        elif selected_tool == "XAMPP":
            install_xampp("https://www.apachefriends.org/index.html")
        elif selected_tool == "Laragon":
            if os_type == "Windows":
                open_url("https://github.com/leokhoa/laragon/releases/tag/6.0.0")
            else:
                print("❌ Laragon hanya support di Windows!!")

    except Exception as e:
        print(f"⚠️ Error: {e}")

def open_url(url):
    os.system(f"start {url}" if os.name == "nt" else f"xdg-open {url}")

def install_node(os_type):
    if os_type == "macOS":
        subprocess.run(["brew", "install", "nodejs"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "-y", "install", "nodejs"])
    elif os_type == "Windows":
        open_url("https://nodejs.org/en/download/")

def install_vscode(os_type):
    if os_type == "macOS":
        subprocess.run(["brew", "install", "--cask", "visual-studio-code"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "snap", "install", "--classic", "code"])
    elif os_type == "Windows":
        open_url("https://code.visualstudio.com/Download")

def install_git(os_type):
    if os_type == "macOS":
        subprocess.run(["brew", "install", "git"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "git"])
    elif os_type == "Windows":
        open_url("https://git-scm.com/download/win")

def install_python(os_type):
    if os_type == "macOS":
        subprocess.run(["brew", "install", "python@3.14"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "python3", "python3-pip"])
    elif os_type == "Windows":
        open_url("https://www.python.org/downloads/windows")
