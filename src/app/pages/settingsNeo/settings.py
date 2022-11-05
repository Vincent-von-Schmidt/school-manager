from PyQt6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QStackedWidget
)
from src.app.pages.settingsNeo.menu import SettingsMenu
from src.app.pages.settingsNeo.pages.general import General


class Settings(QFrame):
    def __init__(self) -> None:
        super().__init__()
        
        self.layout = QVBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.stack.addWidget(menu := SettingsMenu())
        self.stack.addWidget(general := General())
        self.stack.addWidget(QFrame())

        menu.button_general.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        menu.button_design.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        general.button_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)

    def check_settings(self) -> None:
        """
        Check recursive if any settings changed.
        """
        pass
