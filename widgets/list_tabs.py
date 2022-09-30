from PyQt6.QtWidgets import (
    QWidget, 
    QStackedWidget, 
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem
)
from PyQt6.QtGui import QIcon

class ListTabs(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.counter = 0

        self.hLayout = QHBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.vLayout = QVBoxLayout(self)

        self.vLayout.addWidget(list := QListWidget())
        self.list = list

        self.hLayout.addLayout(self.vLayout, 0)
        self.hLayout.addWidget(self.stack, 1)

        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)

        self.setLayout(self.hLayout)

    def addWidget(self, text: str, widget: QWidget, icon: QIcon = None) -> None:
        self.list.insertItem(self.counter, item := QListWidgetItem(text))

        if icon is not None:
            item.setIcon(icon)
            
        self.stack.addWidget(widget)
        self.counter += 1

    def addWidget_left(self, widget: QWidget) -> None:
        self.vLayout.addWidget(widget)
