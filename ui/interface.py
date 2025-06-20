from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt 
from pyfiglet import Figlet
import platform

console = Console()

def show_logo():
    figlet = Figlet(font='block')
    ascii_logo = figlet.renderText('Initium')
    console.print(Panel.fit(
        f"[cyan]{ascii_logo}[/cyan]",
        title="[bold green]INITIUM CLI INSTALLER",
        subtitle="github.com/aditslowly/initium",
        border_style="bright_blue"
    ))

def show_ui():
    show_logo()

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
    
    choice = Prompt.ask("\n[bold yellow]Pilih tools yang ingin diinstall[/bold yellow]", default="0")

    return os_type, choice