from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)


class MainMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.vLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)

        self.vLayout.addWidget(QLabel("School manager"))

        self.button_timetable = QPushButton("timetable")
        self.button_settings = QPushButton("settings")

        self.hLayout.addWidget(self.button_timetable)
        self.hLayout.addWidget(self.button_settings) 

        self.vLayout.addLayout(self.hLayout)

        self.setLayout(self.vLayout)
