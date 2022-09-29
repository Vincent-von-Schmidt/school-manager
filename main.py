from window import Window
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = Window()

    with open("style/dark.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec())
