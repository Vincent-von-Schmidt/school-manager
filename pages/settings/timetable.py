from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QFrame
)
import widgets.div
from data import translate

class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(div1 := widgets.div.Div())
        div1.addWidget(QLabel(translate("div 1")))

        self.layout.addWidget(div2 := widgets.div.Div())
        div2.addWidget(QLabel(translate("div 2")))

        self.setLayout(self.layout)
