from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QFrame
)


class Preferences(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("color mode"))

        self.light_dark_switcher = QComboBox()
        self.light_dark_switcher.addItem("light")
        self.light_dark_switcher.addItem("dark")

        self.layout.addWidget(self.light_dark_switcher)

        self.setLayout(self.layout)
