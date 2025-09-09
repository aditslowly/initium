from ui.gui import show_gui
from package.checker import is_connected
from package.installer import handle_choice
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    if not is_connected():
        print("❌ Tidak ada koneksi internet. Harap sambungkan dan coba lagi.")
        return

    show_gui()


if __name__ == "__main__":
    try:
        show_gui()
    except KeyboardInterrupt:
        print("\n❌ Program diberhentikan oleh user")
