from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
)
import widgets.div


class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.div = widgets.div.Div()

        self.div.addWidget(QLabel("Hello World"))

        self.layout.addWidget(self.div)

        self.setLayout(self.layout)
