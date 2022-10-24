from src.app.window import Window
from PyQt6.QtWidgets import QApplication
import sys
import src.data as data

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = Window()
    
    with open("src/app/style/dark.css", "r") as file:
        style = file.read()
    
    if data.debug:
        with open("src/app/style/debug.css", "r") as file:
            style += file.read()

    app.setStyleSheet(style)

    sys.exit(app.exec())
