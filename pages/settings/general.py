from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QFrame, QRadioButton
)
import data

class General(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("general"))

        self.layout.addWidget(debug_button := QRadioButton(data.translate("debug")))

        self.setLayout(self.layout)
