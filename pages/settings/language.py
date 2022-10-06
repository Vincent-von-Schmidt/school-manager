from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QFrame
)
from data import translate

class Language(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel(translate("language")))

        self.lang_switcher = QComboBox(self)
        self.lang_switcher.addItem(translate("english"))
        self.lang_switcher.addItem(translate("german"))

        # self.lang_switcher.currentIndexChanged(lambda: print(self.lang_switcher.currentText()))

        self.layout.addWidget(self.lang_switcher)

        self.setLayout(self.layout)
