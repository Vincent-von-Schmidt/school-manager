from PyQt6.QtWidgets import (
    QVBoxLayout, 
    QLabel, 
    QPushButton, 
    QFrame, 
    QScrollArea, 
    QScrollBar,
    QGroupBox
)
from src.widgets.div import Div
from src.data import translate


class Timetable(QFrame):
    """
    Settings page for the timetable. 
    """
    def __init__(self) -> None:
        super().__init__()

        scroll_area = QScrollArea(self)
        scroll_area.setVerticalScrollBar(QScrollBar(self))
        scroll_area.setWidgetResizable(True)

        frame = QGroupBox(self)
        self.frame_layout = QVBoxLayout(frame)

        self.frame_layout.addWidget(div1 := Div())
        div1.addWidget(QLabel(translate("div 1")))

        self.frame_layout.addWidget(div2 := Div())
        div2.addWidget(QLabel(translate("div 2")))

        self.frame_layout.addWidget(div3 := Div())
        div3.addWidget(QLabel(translate("div 3")))

        self.frame_layout.addWidget(div4 := Div())
        div4.addWidget(QLabel(translate("div 4")))

        self.frame_layout.addWidget(div5 := Div())
        div5.addWidget(QLabel(translate("div 5")))

        frame.setLayout(self.frame_layout)

        scroll_area.setWidget(frame)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(scroll_area)

        self.setLayout(self.layout)
