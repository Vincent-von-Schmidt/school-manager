from PyQt6.QtWidgets import (
        QFrame,
        QVBoxLayout,
        QLabel,
        QWidget,
        QPushButton
)
from data import translate


class Page(QFrame):
    def __init__(self, headline: str) -> None:
        super().__init__()

        headline: QLabel = QLabel(headline) 
        headline.setObjectName("page_headline")

        body: QFrame = QFrame(self)

        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.layout.addWidget(headline)
        self.layout.addWidget(body)
        self.setLayout(self.layout)

        self.body_layout: QVBoxLayout = QVBoxLayout(body)
        body.setLayout(self.body_layout)

        button_back: QPushButton = QPushButton(translate("back"))
        self.layout.addWidget(button_back)

    def addWidget(self, widget: QWidget) -> None:
        self.body_layout.addWidget(widget)
