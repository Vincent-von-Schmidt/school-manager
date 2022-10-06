from window import Window
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import sys
import data

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = Window()
    
    with open("style/dark.css", "r") as file:
        style = file.read()
    
    if data.debug:
        with open("style/debug.css", "r") as file:
            style += file.read()

    app.setStyleSheet(style)

    sys.exit(app.exec())
