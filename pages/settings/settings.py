from PyQt6.QtWidgets import (
    QWidget, 
    QStackedWidget, 
    QHBoxLayout,
    QListWidget, 
    QVBoxLayout, 
    QPushButton
)
import pages.settings.general
import pages.settings.language
import pages.settings.preferences
import pages.settings.timetable


class Settings(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.vLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.list = QListWidget()
        self.list.insertItem(0, "general")
        self.list.insertItem(1, "preferences")
        self.list.insertItem(2, "timetable")
        self.list.insertItem(3, "language")

        self.hLayout.addWidget(self.list, 0)
        
        self.general = pages.settings.general.General()
        self.preferences = pages.settings.preferences.Preferences()
        self.timetable = pages.settings.timetable.Timetable()
        self.language = pages.settings.language.Language()

        self.stack.addWidget(self.general)
        self.stack.addWidget(self.preferences)
        self.stack.addWidget(self.timetable)
        self.stack.addWidget(self.language)

        self.hLayout.addWidget(self.stack, 1)

        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)

        self.vLayout.addLayout(self.hLayout)

        self.button = QPushButton("back to main menu")
        self.vLayout.addWidget(self.button)

        self.setLayout(self.vLayout)
