from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
)


class MainMenu(QFrame):
    def __init__(self, lang: dict) -> None:
        super().__init__()

        self.vLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)

        self.vLayout.addWidget(QLabel("School manager"))

        self.button_timetable = QPushButton(lang["timetable"])
        self.button_timetable.setObjectName("highlight")

        self.button_settings = QPushButton(lang["settings"])

        self.hLayout.addWidget(self.button_timetable)
        self.hLayout.addWidget(self.button_settings) 

        self.vLayout.addLayout(self.hLayout)
        
        self.setLayout(self.vLayout)
