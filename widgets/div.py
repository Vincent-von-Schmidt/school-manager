from PyQt6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QScrollArea
)


class Div(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setObjectName("div") # css ident 
