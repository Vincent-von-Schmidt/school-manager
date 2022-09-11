from PyQt6.QtWidgets import (
    QWidget, 
    QHBoxLayout
)


class Div(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setObjectName("div") # css ident 

        self.layout = QHBoxLayout(self)

        self.setLayout(self.layout)

    def addWidget(self, widget: QWidget) -> None:
        self.layout.addWidget(widget)
