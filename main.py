from window import Window
from PyQt6.QtWidgets import QApplication
import sys
import json

if __name__ == "__main__":
    app = QApplication([sys.argv])

    with open("lang/en_us.json", "r") as file:
        window = Window(lang=json.loads(file.read()))

    with open("style/dark.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec())
