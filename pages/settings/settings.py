from PyQt6.QtWidgets import (
    QVBoxLayout, 
    QPushButton,
    QFrame
)
from PyQt6.QtGui import QIcon

import pages.settings.general
import pages.settings.language
import pages.settings.preferences
import pages.settings.timetable

import widgets.list_tabs

from data import translate


class Settings(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.list = widgets.list_tabs.ListTabs()
        self.list.addWidget(translate("general"), pages.settings.general.General(), QIcon("assets/settings.ico"))
        self.list.addWidget(translate("design"), pages.settings.preferences.Preferences())
        self.list.addWidget(translate("timetable"), pages.settings.timetable.Timetable())
        self.list.addWidget(translate("language"), pages.settings.language.Language())

        self.layout.addWidget(self.list)

        self.button = QPushButton(translate("back"))
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
