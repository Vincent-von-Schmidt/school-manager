from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea
)
from src.widgets.div import Div
from src.data import translate


class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(div1 := Div())
        div1.addWidget(QLabel(translate("div 1")))

        self.layout.addWidget(div2 := Div())
        div2.addWidget(QLabel(translate("div 2")))

        self.layout.addWidget(div3 := Div())
        div3.addWidget(QLabel(translate("div 3")))

        self.layout.addWidget(div4 := Div())
        div4.addWidget(QLabel(translate("div 4")))

        self.layout.setSpacing(0)

        self.setLayout(self.layout)
        self.show()
