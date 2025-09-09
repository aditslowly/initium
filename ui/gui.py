import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import threading, time, platform

from package import installer

# ==== DETEKSI OS SEKALI ====
os_type = platform.system()
if os_type == "Darwin":
    os_type = "macOS"
elif os_type == "Linux":
    os_type = "Linux"
elif os_type == "Windows":
    os_type = "Windows"

# ==== TOOLS & MAPPING ====
TOOLS = {
    "Browsers": ["Brave", "Chrome", "Firefox", "Opera GX", "Vivaldi"],
    "Communications": ["Discord", "Notion", "Zoom", "Telegram"],
    "Development": [
        "Neovim", "Git", "Docker", "Node.js", "Python",
        "Visual Studio Code", "PHP (Laragon)", "Postman",
        "Sublime Text", "Composer", "XAMPP", "Laragon"
    ]
}

INSTALLER_MAP = {
    "Node.js": installer.install_node,
    "Visual Studio Code": installer.install_vscode,
    "Git": installer.install_git,
    "Python": installer.install_python,
    "XAMPP": installer.install_xampp,
    "Laragon": installer.install_laragon,
    "Postman": installer.install_postman,
    "Docker": installer.install_docker,
    "PHP (Laragon)": installer.install_php_laragon,
    "Composer": installer.install_composer,
    # contoh tambahan apps dummy:
    "Brave": installer.install_brave,
    "Chrome": lambda os_type: print("➡️ Install Chrome (belum diimplementasi)"),
    "Firefox": lambda os_type: print("➡️ Install Firefox (belum diimplementasi)"),
    "Opera GX": lambda os_type: print("➡️ Install Opera GX (belum diimplementasi)"),
    "Vivaldi": lambda os_type: print("➡️ Install Vivaldi (belum diimplementasi)"),
    "Discord": lambda os_type: print("➡️ Install Discord (belum diimplementasi)"),
    "Notion": lambda os_type: print("➡️ Install Notion (belum diimplementasi)"),
    "Zoom": lambda os_type: print("➡️ Install Zoom (belum diimplementasi)"),
    "Telegram": lambda os_type: print("➡️ Install Telegram (belum diimplementasi)"),
    "Neovim": lambda os_type: print("➡️ Install Neovim (belum diimplementasi)"),
    "Sublime Text": lambda os_type: print("➡️ Install Sublime Text (belum diimplementasi)"),
}

def show_gui():
    app = tb.Window(themename="journal")
    app.title("Initium")
    app.geometry("1200x600")

    # == Sidebar ==
    sidebar = tk.Frame(app, bg="#1c1c1c", width=200)
    sidebar.pack(side="left", fill="y")

    actions = [
        ("Install/Upgrade Applications", lambda: print("Install clicked")),
        ("Uninstall Applications", lambda: print("Uninstall clicked")),
        ("Upgrade all Applications", lambda: print("Upgrade clicked")),
    ]

    tk.Label(sidebar, text="Actions", fg="white", bg="#1c1c1c", 
             font=("sans-serif", 16)).pack(pady=(15, 5))
    
    for text, cmd in actions:
        btn = tb.Button(sidebar, text=text, bootstyle="primary", command=cmd)
        btn.pack(pady=5, fill="x", padx=10)
    
    # == Tabs Atas ==
    notebook = tb.Notebook(app, bootstyle="dark")
    notebook.pack(side="right", fill="both", expand=True)

    tab_install = tb.Frame(notebook)
    notebook.add(tab_install, text="Install")

    # == Konten tab Install ==
    canvas = tk.Canvas(tab_install)
    scroll = tk.Scrollbar(tab_install, orient="vertical", command=canvas.yview)
    scroll_frame = tb.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)

    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    check_vars = []
    for category, tools in TOOLS.items():
        lbl = tk.Label(scroll_frame, text=category,
                       font=("sans-serif", 16), anchor="w")
        lbl.pack(fill="x", pady=(10, 2))

        frame = tb.Frame(scroll_frame)
        frame.pack(fill="x", padx=15, pady=5)

        for idx, tool in enumerate(tools):
            var = tk.BooleanVar()
            row, col = divmod(idx, 5)
            chk = tb.Checkbutton(frame, text=tool, variable=var, bootstyle="success")
            chk.grid(row=row, column=col, padx=10, pady=5, sticky="w")
            check_vars.append((tool, var))

    # Progress bar + status
    progress = tb.Progressbar(scroll_frame, bootstyle="success-striped", length=500, mode="determinate")
    progress.pack(pady=10)
    
    status_label = tb.Label(scroll_frame, text="Pilih Aplikasi yang Ingin Di Install", font=("sans-serif", 12))
    status_label.pack()

    # == Log box ==
    log_box = tk.Text(scroll_frame, height=10, wrap="word", state="disabled", bg="#1e1e1e", fg="white")
    log_box.pack(fill="both", padx=10, pady=10, expand=True)

    def log_message(msg: str):
        log_box.config(state="normal")
        log_box.insert("end", msg + "\n")
        log_box.see("end")
        log_box.config(state="disabled")

    def run_progress(selected):
        total_apps = len(selected)
        progress["value"] = 0
        step = 100 / total_apps

        for idx, app_name in enumerate(selected, start=1):
            for i in range(101):
                time.sleep(0.02)  # simulasi progress
                progress["value"] = ((idx - 1) * step) + (i / 100 * step)
                status_label.config(text=f"Installing {app_name}... {int(progress['value'])}%")
                app.update_idletasks()

            # Panggil installer beneran
            if app_name in INSTALLER_MAP:
                try:
                    INSTALLER_MAP[app_name](os_type)
                    log_message(f"✅ {app_name} berhasil diinstall")
                except Exception as e:
                    log_message(f"❌ {app_name} gagal diinstall: {e}")
            else:
                log_message(f"⚠️ {app_name} belum tersedia installernya")

        status_label.config(text=f"Selesai ✅: {', '.join(selected)}")
        log_message("=== Semua aplikasi selesai diinstall ===")

    def on_install():
        selected = [tool for tool, var in check_vars if var.get()]
        if not selected:
            status_label.config(text="❗ Pilih minimal satu aplikasi dulu")
            return
        threading.Thread(target=run_progress, args=(selected,), daemon=True).start()

    btn_install = tb.Button(scroll_frame, text="Install", bootstyle="success", command=on_install)
    btn_install.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    show_gui()
