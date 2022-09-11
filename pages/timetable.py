from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)


class Timetable(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("timetable"))

        self.button = QPushButton("back to main menu")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
