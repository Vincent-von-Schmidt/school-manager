from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QFrame
)
from src.data import translate


class SettingsMenu(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout: QVBoxLayout = QVBoxLayout(self)

        self.button_general: QPushButton = QPushButton(translate("General"))
        self.layout.addWidget(self.button_general)
        self.button_general.setObjectName("div")

        self.button_design: QPushButton = QPushButton(translate("Design"))
        self.layout.addWidget(self.button_design)
        self.button_design.setObjectName("div")

        self.button_save: QPushButton = QPushButton(translate("Save"))
        self.layout.addWidget(self.button_save)
        self.button_save.setObjectName("highlight")

        self.setLayout(self.layout)
