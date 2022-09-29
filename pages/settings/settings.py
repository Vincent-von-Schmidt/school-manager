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


class Settings(QFrame):
    def __init__(self, lang: dict, config: dict) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.list = widgets.list_tabs.ListTabs()
        self.list.addWidget(lang["general"], pages.settings.general.General(lang=lang, config=config), QIcon("assets/settings.ico"))
        self.list.addWidget(lang["design"], pages.settings.preferences.Preferences(lang=lang, config=config))
        self.list.addWidget(lang["timetable"], pages.settings.timetable.Timetable(lang=lang, config=config))
        self.list.addWidget(lang["language"], pages.settings.language.Language(lang=lang, config=config))

        self.layout.addWidget(self.list)

        self.button = QPushButton(lang["back"])
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
