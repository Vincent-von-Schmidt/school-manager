from PyQt6.QtWidgets import (
    QVBoxLayout, 
    QLabel, 
    QFrame 
)
from src.widgets.div.div import Div
from src.data import translate


class Timetable(QFrame):
    """
    Settings page for the timetable. 
    """
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

        self.layout.addWidget(div5 := Div())
        div5.addWidget(QLabel(translate("div 5")))

        self.setLayout(self.layout)
