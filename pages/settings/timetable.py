from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QFrame
)
import widgets.div
from data import translate

class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.div = widgets.div.Div()

        self.div.addWidget(QLabel(translate("Hello World!")))

        self.layout.addWidget(self.div)

        self.setLayout(self.layout)
