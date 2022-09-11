from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)


class Preferences(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("preferences"))

        self.setLayout(self.layout)
