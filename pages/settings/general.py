from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)


class General(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("general"))

        self.setLayout(self.layout)
