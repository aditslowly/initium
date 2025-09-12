import subprocess
import os
import webbrowser
import platform
<<<<<<< HEAD
import time
=======
>>>>>>> 802128f (back to cli basic)
from .php_installer import (
    download_and_install_php,
    is_laragon_installed,
    detect_installed_php_versions,
    SUPPORTED_PHP_VERSIONS,
)


<<<<<<< HEAD
# === HELPER UNTUK CALLBACK ===
def update_progress(progress_callback, value):
    if progress_callback:
        progress_callback(value)


def log_message(log_callback, message):
    if log_callback:
        log_callback(message)


# === MAIN HANDLER ===
def handle_choice(choice, os_type, progress_callback=None, log_callback=None):
=======
def handle_choice(choice, os_type):
>>>>>>> 802128f (back to cli basic)
    tools = {
        1: {"name": "Node.js", "install": install_node},
        2: {"name": "Visual Studio Code", "install": install_vscode},
        3: {"name": "Git", "install": install_git},
        4: {"name": "Python", "install": install_python},
        5: {"name": "XAMPP", "install": install_xampp},
        6: {"name": "Laragon", "install": install_laragon},
        7: {"name": "Postman", "install": install_postman},
        8: {"name": "Docker Desktop", "install": install_docker},
        9: {"name": "PHP untuk laragon", "install": install_php_laragon},
        10: {"name": "Composer", "install": install_composer},
<<<<<<< HEAD
=======
        11: {"name": "Install Semua", "install": None},
        12: {"name": "Keluar", "install": None},
>>>>>>> 802128f (back to cli basic)
    }

    try:
        choice = int(choice)

        if os_type == "Windows" and not is_winget_available():
<<<<<<< HEAD
            log_message(log_callback, "❌ Winget tidak tersedia di sistem, fallback URL akan digunakan")
            return

        if choice == 0:
            log_message(log_callback, "👋🏻 Keluar dari program!")
            exit()

        if choice == 11:  # install semua
            for i in tools:
                tool = tools[i]
                log_message(log_callback, f"🔧 Menginstall {tool['name']}...")
                tool["install"](os_type, progress_callback, log_callback)
            log_message(log_callback, "\n✅ Semua tools berhasil diproses")
=======
            print("❌ Winget tidak tersedia disistem, akan menggunakan fallback URL")
            return

        if choice == 12:
            print("👋🏻 Keluar dari program!")
            return

        if choice == 11:
            for i in range(1, 10):
                print(f"🔧 Menginstall {tools[i]['name']}...")
                tools[i]["install"](os_type)
            print("\n✅ Semua tools berhasil diproses")
>>>>>>> 802128f (back to cli basic)
            return

        selected = tools.get(choice)
        if not selected:
<<<<<<< HEAD
            log_message(log_callback, "⚠️ Pilihan tidak valid!")
            return

        log_message(log_callback, f"🛠 Menginstall {selected['name']}...\n")
        selected["install"](os_type, progress_callback, log_callback)

    except Exception as e:
        log_message(log_callback, f"⚠️ Error: {e}")
=======
            print("⚠️ Pilihan tidak valid!")
            return

        print(f"🛠 Menginstall {selected['name']}...\n")
        selected["install"](os_type)

    except Exception as e:
        print(f"⚠️ Error: {e}")
>>>>>>> 802128f (back to cli basic)


# === DETEKSI WINGET HELPER ===
def is_winget_available():
    return (
        subprocess.call(
            ["where", "winget"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        == 0
    )


<<<<<<< HEAD
def winget_install(package_id, fallback_url=None, progress_callback=None, log_callback=None):
    if not is_winget_available():
        if fallback_url:
            log_message(log_callback, f"🔗 Membuka Fallback URL untuk {package_id}")
            open_url(fallback_url)
        else:
            log_message(log_callback, f"❌ Winget dan fallback URL tidak tersedia untuk {package_id}")
=======
def winget_install(package_id, fallback_url=None):
    if not is_winget_available():
        if fallback_url:
            print(f"🔗 Membuka Fallback URL untuk {package_id}")
            open_url(fallback_url)
        else:
            print("❌ Winget dan fallback URL tidak tersedia untuk {package_id}")
>>>>>>> 802128f (back to cli basic)
        return

    try:
        subprocess.run(
            [
                "winget",
                "install",
                "--id",
                package_id,
                "--source",
                "winget",
                "--silent",
                "--accept-package-agreements",
                "--accept-source-agreements",
                "-e",
            ],
            check=True,
        )
<<<<<<< HEAD
        update_progress(progress_callback, 100)
        log_message(log_callback, f"✅ {package_id} berhasil diinstall")
    except subprocess.CalledProcessError:
        log_message(log_callback, f"⚠️ Winget gagal menginstall {package_id}")
=======
    except subprocess.CalledProcessError:
        print(f"⚠️ Winget gagal menemukan atau menginstall {package_id}")
>>>>>>> 802128f (back to cli basic)
        if fallback_url:
            open_url(fallback_url)


# === FUNGSI PEMBANTU ===
def open_url(url):
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(url)
        elif system == "Darwin":
            subprocess.run(["open", url])
        elif system == "Linux":
            subprocess.run(["xdg-open", url])
        else:
            webbrowser.open(url)
    except Exception as e:
        print(f"❌ Gagal membuka URL: {e}")


# === INSTALLER FUNCTION ===
<<<<<<< HEAD
def install_node(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Node.js...")
    update_progress(progress_callback, 10)
    time.sleep(0.5)

    if os_type == "macOS":
        subprocess.run(["brew", "install", "node"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "nodejs"])
    elif os_type == "Windows":
        winget_install("OpenJS.NodeJS", "https://nodejs.org/en/download/",
                       progress_callback, log_callback)

    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Node.js berhasil diinstall")


def install_vscode(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Visual Studio Code...")
    update_progress(progress_callback, 10)

    if os_type == "Windows":
        winget_install("Microsoft.VisualStudioCode",
                       "https://code.visualstudio.com/Download",
                       progress_callback, log_callback)
=======
def install_node(os_type):
    if os_type == "macOS":
        subprocess.run(["brew", "install", "nodejs"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "nodejs"])
    elif os_type == "Windows":
        winget_install("OpenJS.NodeJS", "https://nodejs.org/en/download/")


def install_vscode(os_type):
    if os_type == "Windows":
        winget_install(
            "Microsoft.VisualStudioCode", "https://code.visualstudio.com/Download"
        )
>>>>>>> 802128f (back to cli basic)
    elif os_type == "macOS":
        subprocess.run(["brew", "install", "--cask", "visual-studio-code"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "snap", "install", "--classic", "code"])

<<<<<<< HEAD
    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Visual Studio Code berhasil diinstall")


def install_git(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Git...")
    update_progress(progress_callback, 10)

    if os_type == "Windows":
        winget_install("Git.Git", "https://git-scm.com/download/win",
                       progress_callback, log_callback)
=======

def install_git(os_type):
    if os_type == "Windows":
        winget_install("Git.Git", "https://git-scm.com/download/win")
>>>>>>> 802128f (back to cli basic)
    elif os_type == "macOS":
        subprocess.run(["brew", "install", "git"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "git"])

<<<<<<< HEAD
    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Git berhasil diinstall")


def install_python(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Python...")
    update_progress(progress_callback, 10)

    if os_type == "Windows":
        winget_install("Python.Python.3.13",
                       "https://www.python.org/downloads/windows",
                       progress_callback, log_callback)
=======

def install_python(os_type):
    if os_type == "Windows":
        winget_install("Python.Python3.13", "https://www.python.org/downloads/windows")
>>>>>>> 802128f (back to cli basic)
    elif os_type == "macOS":
        subprocess.run(["brew", "install", "python@3.14"])
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "python3", "python3-pip"])

<<<<<<< HEAD
    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Python berhasil diinstall")


def install_xampp(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "🌐 Membuka halaman XAMPP...")
    open_url("https://www.apachefriends.org/index.html")
    update_progress(progress_callback, 100)


def install_laragon(os_type, progress_callback=None, log_callback=None):
    if os_type != "Windows":
        log_message(log_callback, "❌ Laragon hanya tersedia di Windows")
        return

    log_message(log_callback, "⬇️ Mengunduh dan menginstall Laragon..")
    update_progress(progress_callback, 20)
=======

def install_xampp(os_type):
    open_url("https://www.apachefriends.org/index.html")


def install_laragon(os_type):
    if os_type != "Windows":
        print("❌ Laragon hanya tersedia di Windows")
        return

    print("⬇️ Mengunduh dan menginstall Laragon..")
>>>>>>> 802128f (back to cli basic)

    installer_url = (
        "https://github.com/leokhoa/laragon/releases/download/6.0.0/laragon-wamp.exe"
    )
    installer_name = "laragon-wamp.exe"

    try:
        import urllib.request

        urllib.request.urlretrieve(installer_url, installer_name)
<<<<<<< HEAD
        update_progress(progress_callback, 60)
        log_message(log_callback, "✅ Laragon berhasil diunduh")

        log_message(log_callback, "🚀 Membuka installer Laragon...")
        os.startfile(installer_name)
        update_progress(progress_callback, 100)
    except Exception as e:
        log_message(log_callback, f"❌ Gagal menginstall Laragon: {e}")


def install_postman(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Postman...")

    if os_type == "Windows":
        winget_install("Postman.Postman", "https://www.postman.com/downloads",
                       progress_callback, log_callback)
    else:
        open_url("https://www.postman.com/downloads")

    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Postman siap digunakan")


def install_docker(os_type, progress_callback=None, log_callback=None):
    log_message(log_callback, "⬇️ Menginstall Docker Desktop...")
    update_progress(progress_callback, 10)

    if os_type == "Windows":
        winget_install("Docker.DockerDesktop",
                       "https://www.docker.com/products/docker-desktop/",
                       progress_callback, log_callback)
=======
        print("✅ Laragon berhasil di unduh")

        print("🚀 Membuka installer Laragon...")
        os.startfile(installer_name)

    except Exception as e:
        print(f"❌ Gagal menginstall Laragon: {e}")


def install_postman(os_type):
    if os_type == "Windows":
        winget_install("Postman.Postman", "https://www.postman.com/downloads")
    else:
        open_url("https://www.postman.com/downloads")


def install_docker(os_type):
    if os_type == "Windows":
        winget_install(
            "Docker.DockerDesktop", "https://www.docker.com/products/docker-dekstop/"
        )
>>>>>>> 802128f (back to cli basic)
    elif os_type == "macOS":
        open_url("https://www.docker.com/products/docker-desktop/")
    elif os_type == "Linux":
        subprocess.run(["sudo", "apt", "install", "-y", "docker.io"])

<<<<<<< HEAD
    update_progress(progress_callback, 100)
    log_message(log_callback, "✅ Docker berhasil diinstall")


def install_php_laragon(os_type, progress_callback=None, log_callback=None):
    if os_type != "Windows":
        log_message(log_callback, "❌ Fitur ini hanya tersedia di Windows.")
        return

    if not is_laragon_installed():
        log_message(log_callback, "❌ Laragon tidak ditemukan di sistem.")
        return

    log_message(log_callback, "--- PHP Installer Untuk Laragon ---")
    detect_installed_php_versions()

    version = "8.2"  # default versi (nanti bisa ambil input GUI)
    try:
        download_and_install_php(version, progress_callback=progress_callback,
                                 log_callback=log_callback)
        log_message(log_callback, f"✅ PHP {version} berhasil ditambahkan ke Laragon")
    except Exception as e:
        log_message(log_callback, f"❌ Gagal menginstall PHP: {e}")


def install_composer(os_type, progress_callback=None, log_callback=None):
    if os_type != "Windows":
        log_message(log_callback, "❌ Composer installer .exe hanya tersedia di Windows")
        return

    log_message(log_callback, "⬇️ Mengunduh installer Composer.")
=======

def install_php_laragon(os_type):
    if os_type != "Windows":
        print("❌ Fitur ini hanya tersedia di Windows.")
        return

    if not is_laragon_installed():
        print("❌ Laragon tidak ditemukan di sistem, harap install terlebih dahulu.")

    print("\n--- PHP Installer Untuk Laragon ---")
    detect_installed_php_versions()

    print("\nVersi yang tersedia untuk di unduh: ")
    for key, val in SUPPORTED_PHP_VERSIONS.items():
        print(f"{key} -> PHP {val}")

    version = input("\nMasukkan versi PHP yang ingin di unduh (misal 8.3).").strip()
    download_and_install_php(version)


def install_composer(os_type):
    if os_type != "Windows":
        print("❌ Composer installer .exe hanya tersedia di Windows")
        return

    print("⬇️ Mengunduh installer composer.")
>>>>>>> 802128f (back to cli basic)
    composer_url = "https://getcomposer.org/Composer-Setup.exe"
    installer_path = "Composer-Setup.exe"

    try:
        import urllib.request

        urllib.request.urlretrieve(composer_url, installer_path)
<<<<<<< HEAD
        update_progress(progress_callback, 60)
        log_message(log_callback, "✅ Composer installer berhasil diunduh")

        log_message(log_callback, "🚀 Menjalankan installer Composer...")
        os.startfile(installer_path)
        update_progress(progress_callback, 100)
    except Exception as e:
        log_message(log_callback, f"❌ Gagal menginstall Composer: {e}")
=======
        print("✅ Composer installer berhasil di unduh")

        print("🚀 Menjalankan installer Composer...")
        os.startfile(installer_path)
    except Exception as e:
        print(f"❌ Gagal menginstall Composer: {e}")
>>>>>>> 802128f (back to cli basic)
