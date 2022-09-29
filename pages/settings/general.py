from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
)


class General(QFrame):
    def __init__(self, lang: dict, config: dict) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("general"))

        self.setLayout(self.layout)
