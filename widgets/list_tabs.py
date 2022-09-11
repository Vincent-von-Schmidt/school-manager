from PyQt6.QtWidgets import (
    QWidget, 
    QStackedWidget, 
    QHBoxLayout,
    QListWidget,
    QListWidgetItem
)
from PyQt6.QtGui import QIcon

class ListTabs(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.counter = 0

        self.layout = QHBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.list = QListWidget()

        self.layout.addWidget(self.list, 0)
        self.layout.addWidget(self.stack, 1)

        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)

        self.setLayout(self.layout)

    def addWidget(self, text: str, widget: QWidget, icon: QIcon = None) -> None:
        self.list.insertItem(self.counter, item := QListWidgetItem(text))

        if icon is not None:
            item.setIcon(icon)
            
        self.stack.addWidget(widget)
        self.counter += 1
