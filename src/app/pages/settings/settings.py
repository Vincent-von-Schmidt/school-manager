from PyQt6.QtWidgets import (
    QVBoxLayout, 
    QPushButton,
    QFrame
)
from PyQt6.QtGui import QIcon

from src.app.pages.settings.general import General
from src.app.pages.settings.language import Language
from src.app.pages.settings.preferences import Preferences
from src.app.pages.settings.timetable import Timetable

from src.widgets.list_tabs import ListTabs

from src.data import translate, safe_config


class Settings(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.list = ListTabs()
        self.list.addWidget(translate("general"), General(), QIcon("assets/settings.ico"))
        self.list.addWidget(translate("design"), Preferences())

        # self.list.addWidget(translate("timetable"), timetable_scroll := QScrollArea(self))
        # timetable_scroll.setWidget(Timetable())

        self.list.addWidget(translate("timetable"), Timetable())

        self.list.addWidget(translate("language"), Language())

        self.list.addWidget_left(save_button := QPushButton(translate("save")))
        save_button.setObjectName("highlight")
        save_button.clicked.connect(lambda: safe_config())

        self.layout.addWidget(self.list)

        self.button = QPushButton(translate("back"))
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
