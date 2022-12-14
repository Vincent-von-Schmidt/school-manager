from app.window import Window
from PyQt6.QtWidgets import QApplication
import sys
import data as data

if __name__ == "__main__":
    app: QApplication = QApplication([sys.argv])
    window: Window = Window()
    
    with open("app/style/dark.css", "r") as file:
        style: str = file.read()
    
    if data.debug:
        with open("app/style/debug.css", "r") as file:
            style += file.read()

    app.setStyleSheet(style)

    sys.exit(app.exec())
