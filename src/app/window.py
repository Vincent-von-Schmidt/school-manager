from PyQt6.QtWidgets import (
    QStackedWidget, QVBoxLayout, QFrame
)
from app.pages.main_menu import MainMenu


class Window(QFrame):
    def __init__(self) -> None:
        super().__init__()

        # config
        self.setWindowTitle("School manager")

        self.layout: QVBoxLayout = QVBoxLayout(self)

        self.layout.addWidget(MainMenu())

        # layout config
        self.setLayout(self.layout)
        self.resize(1280, 720)
        self.show()
