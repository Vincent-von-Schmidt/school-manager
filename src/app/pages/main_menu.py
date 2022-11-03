from PyQt6.QtWidgets import QFrame, QVBoxLayout
from PyQt6.QtGui import QIcon
from src.widgets.list_tabs import ListTabs
from src.app.pages.timetable import Timetable
from src.app.pages.settings.settings import Settings


class MainMenu(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(content := ListTabs())
        content.addWidget("Dashboard", QFrame(), QIcon("assets/home.ico"))
        content.addWidget("Timetable", Timetable()) 
        content.addWidget("settings", Settings(), QIcon("assets/settings.ico"))

        self.setLayout(self.layout)
