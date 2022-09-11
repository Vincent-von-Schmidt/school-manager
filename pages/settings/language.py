from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)


class Language(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("language"))

        self.setLayout(self.layout)
