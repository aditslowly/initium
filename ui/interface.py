from rich.console import Console
from rich.panel import Panel
from rich.markup import escape
from rich.prompt import Prompt
from pyfiglet import Figlet
<<<<<<< HEAD
import requests
=======
>>>>>>> 802128f (back to cli basic)
import platform
import os

console = Console()


def show_logo():
    figlet = Figlet(font="standard")
    ascii_logo = escape(figlet.renderText("Initium"))
<<<<<<< HEAD

    console.print(
        Panel.fit(
            f"[blue]{ascii_logo}[/blue]",
            title="[bold blue]INITIUM",
            subtitle="github.com/aditslowly/initium",
            border_style="blue",
=======
    console.print(
        Panel.fit(
            f"[cyan]{ascii_logo}[/cyan]",
            title="[bold green]INITIUM CLI INSTALLER",
            subtitle="github.com/aditslowly/initium",
            border_style="bright_blue",
>>>>>>> 802128f (back to cli basic)
        )
    )


<<<<<<< HEAD
def get_latest_version():
    try:
        url = "https://api.github.com/repos/aditslowly/initium/tags"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        tags = r.json()
        if tags:
            return tags[0]["name"]

    except Exception:
        return "dev"


def show_ui():
    os.system("cls" if os.name == "nt" else "clear")
    show_logo()
=======
def show_ui():
    os.system("cls" if os.name == "nt" else "clear")
    show_logo()

>>>>>>> 802128f (back to cli basic)
    # OS Identify
    os_name = platform.system()
    os_type = "Unknown"

<<<<<<< HEAD
    version = get_latest_version()

=======
>>>>>>> 802128f (back to cli basic)
    # if else condition
    if os_name == "Darwin":
        os_type = "macOS"
    elif os_name == "Windows":
        os_type = "Windows"
<<<<<<< HEAD
    elif os_name == "Linux":
        os_type = "Linux"

    console.print(
        f"\n📦 [bold]Detected OS:[/bold] {os_type}\n", style="bold magenta")

    console.print(
        f"📦 [bold]Major Version: [/bold]{version}\n", style="bold green")
=======
    elif os_name == "Ubuntu":
        os_type = "Linux"

    console.print(f"\n📦 [bold]Detected OS:[/bold] {os_type}\n", style="bold magenta")

>>>>>>> 802128f (back to cli basic)
    tools = [
        "Node.js",
        "Visual Studio Code",
        "Git",
        "Python",
        "XAMPP",
        "Laragon",
        "Postman",
        "Docker Desktop",
        "PHP Laragon",
        "Composer",
        "Install Semua",
        "Keluar",
    ]

    for i, tool in enumerate(tools, 1):
        console.print(f"[bold blue]{i}.[/bold blue] {tool}")

    choice = Prompt.ask(
        "\n[bold yellow]Pilih tools yang ingin diinstall[/bold yellow]", default="0"
    )

    return os_type, choice
