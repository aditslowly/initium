import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from package.installer import handle_choice
from ui.interface import show_ui

def main():
    os_type, choice = show_ui()
    handle_choice(choice, os_type)

if __name__ == "__main__":
    main()