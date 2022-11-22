from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout
)
from src.widgets.list_tabs import ListTabs


class Layout(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.sidebar: ListTabs = ListTabs()

        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.layout.addWidget(self.sidebar)

    def addSection(self) -> None:
        pass


