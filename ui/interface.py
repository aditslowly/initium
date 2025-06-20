from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt 
from pyfiglet import Figlet
import platform

console = Console()

def show_ui():
    figlet = Figlet(font='slant')
    header = figlet.renderText('INITIUM')
    console.print(f"[bold cyan]{header}[/bold cyan]")
    console.print(Panel.fit("INITIUM - Code Setup Installer", style="green"))

    # OS Identify
    os_name = platform.system()
    os_type = "Unknown"

    # if else condition
    if os_name == "Darwin":
        os_type = "macOS"
    elif os_name == "Windows":
        os_type = "Windows"
    elif os_name == "Linux":
        os_type = "Linux"

    console.print(f"\n📦 [bold]Detected OS:[/bold] {os_type}\n", style="bold magenta")

    tools = [
        "Node.js", "Visual Studio Code", "Git", "Python", "XAMPP", "Laragon", "Keluar"
    ]

    for i, tool in enumerate(tools, 1):
        console.print(f"[bold blue]{i}.[/bold blue] {tool}")
    
    choice = Prompt.ask("\n[bold yellow]Pilih tool yang ingin di install[/bold yellow]", default="0")

    return os_type, choice