from PyQt6.QtWidgets import (
    QStackedWidget, QVBoxLayout, QFrame
)
import pages.main_menu
import pages.timetable
import pages.settings.settings


class Window(QFrame):
    def __init__(self, lang: dict, config: dict) -> None:
        super().__init__()

        # config
        self.setWindowTitle("School manager")

        # content
        self.layout = QVBoxLayout(self)
        self.stack = QStackedWidget(self)

        self.main_menu = pages.main_menu.MainMenu(lang=lang, config=config)
        self.timetable = pages.timetable.Timetable(lang=lang, config=config)
        self.settings = pages.settings.settings.Settings(lang=lang, config=config)
        
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.timetable)
        self.stack.addWidget(self.settings)

        # button config
        self.main_menu.button_timetable.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.main_menu.button_settings.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.timetable.button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.settings.button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        # layout config
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        self.resize(1280, 720)
        self.show()
