from PyQt6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QPushButton
)
import pages.settings.general
import pages.settings.language
import pages.settings.preferences
import pages.settings.timetable

import widgets.list_tabs


class Settings(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.list = widgets.list_tabs.ListTabs()

        self.list.addWidget("general", pages.settings.general.General())
        self.list.addWidget("preferences", pages.settings.preferences.Preferences())
        self.list.addWidget("timetable", pages.settings.timetable.Timetable())
        self.list.addWidget("language", pages.settings.language.Language())

        self.layout.addWidget(self.list)

        self.button = QPushButton("back to main menu")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
