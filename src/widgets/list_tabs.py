from PyQt6.QtWidgets import (
    QWidget, 
    QStackedWidget, 
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QScrollArea,
    QScrollBar,
    QFrame
)
from PyQt6.QtGui import QIcon

class ListTabs(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.counter = 0

        self.hLayout = QHBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.vLayout = QVBoxLayout(self)

        self.list = QListWidget()
        self.vLayout.addWidget(self.list)

        self.hLayout.addLayout(self.vLayout, 0)
        self.hLayout.addWidget(self.stack, 1)

        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)

        self.setLayout(self.hLayout)

    def addWidget(self, text: str, widget: QWidget, icon: QIcon = None) -> None:
        self.list.insertItem(self.counter, item := QListWidgetItem(text))

        # icon check
        if icon is not None:
            item.setIcon(icon)

        # scroll area config
        scroll_area = QScrollArea(self)
        scroll_area.setVerticalScrollBar(QScrollBar(self))
        scroll_area.setWidgetResizable(True)

        # frame + layout creation
        content = QFrame(self)
        layout = QVBoxLayout(content)

        # widget append
        layout.addWidget(widget)

        # add content frame as primary widget 
        content.setLayout(layout)
        scroll_area.setWidget(content)

        # add scroll_area to stack, set counter for list + 1 
        self.stack.addWidget(scroll_area)
        self.counter += 1

