from PyQt6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QStackedWidget
)
from app.pages.settingsNeo.menu import SettingsMenu
from app.pages.settingsNeo.pages.general import General
from widgets.page import Page


class Settings(QFrame):
    def __init__(self) -> None:
        super().__init__()
        
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.stack: QStackedWidget = QStackedWidget(self)

        menu: SettingsMenu = SettingsMenu()
        self.stack.addWidget(menu)

        general: General = General()
        self.stack.addWidget(general)

        test_page: Page = Page("test page")
        self.stack.addWidget(test_page)

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
