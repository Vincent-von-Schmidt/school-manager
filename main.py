from window import Window
from PyQt6.QtWidgets import QApplication
import PyQt6.QtCore
import sys

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = Window()

    window.setContentsMargins(0, 0, 0, 0)

    # style = PyQt6.QtCore.QFile("style/dark.qss")
    # style.open(PyQt6.QtCore.QIODevice.readonly)
    # app.setStyleSheet(PyQt6.QtCore.QTextStream(style).readAll())

    with open("style/dark.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec())
