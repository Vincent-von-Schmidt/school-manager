from PyQt6.QtWidgets import (
    QVBoxLayout, 
    QPushButton,
    QFrame,
    QScrollArea
)
from PyQt6.QtGui import QIcon, QPalette

import pages.settings.general
import pages.settings.language
import pages.settings.preferences
import pages.settings.timetable

import widgets.list_tabs

from data import translate, safe_config


class Settings(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.list = widgets.list_tabs.ListTabs()
        self.list.addWidget(translate("general"), pages.settings.general.General(), QIcon("assets/settings.ico"))
        self.list.addWidget(translate("design"), pages.settings.preferences.Preferences())
        self.list.addWidget(translate("timetable"), timetable_scroll := QScrollArea(self))
        timetable_scroll.setWidget(pages.settings.timetable.Timetable())
        self.list.addWidget(translate("language"), pages.settings.language.Language())

        self.list.addWidget_left(save_button := QPushButton(translate("save")))
        save_button.setObjectName("highlight")
        save_button.clicked.connect(lambda: safe_config())

        self.layout.addWidget(self.list)

        self.button = QPushButton(translate("back"))
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
