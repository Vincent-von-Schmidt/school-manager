from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QFrame
)
from data import translate

class Preferences(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel(translate("color mode")))

        self.light_dark_switcher = QComboBox()
        self.light_dark_switcher.addItem(translate("light"))
        self.light_dark_switcher.addItem(translate("dark"))

        self.layout.addWidget(self.light_dark_switcher)

        self.setLayout(self.layout)
