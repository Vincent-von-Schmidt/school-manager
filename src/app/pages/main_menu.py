from PyQt6.QtWidgets import QFrame, QVBoxLayout
from PyQt6.QtGui import QIcon
from widgets.list_tabs import ListTabs
from app.pages.timetable import Timetable
from app.pages.settingsNeo.settings import Settings as SettingsNeo
from app.pages.dashboard import Dashboard
from data import translate


class MainMenu(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout: QVBoxLayout = QVBoxLayout(self)

        content: ListTabs = ListTabs() 
        content.addWidget(translate("Dashboard"), Dashboard(), QIcon("assets/home.ico"))
        content.addWidget(translate("Timetable"), Timetable()) 
        content.addWidget(translate("Settings"), SettingsNeo(), QIcon("assets/settings.ico"))
        self.layout.addWidget(content)

        self.setLayout(self.layout)
