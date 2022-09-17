from PyQt6.QtWidgets import (
    QWidget, 
    QHBoxLayout,
    QFrame
)

class Div(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QHBoxLayout(self)

        self.setLayout(self.layout)

    def addWidget(self, widget: QWidget) -> None:
        self.layout.addWidget(widget)
