from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QFrame
)


class Language(QFrame):
    def __init__(self, lang: dict, config: dict) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("language"))

        self.lang_switcher = QComboBox(self)
        self.lang_switcher.addItem("English")
        self.lang_switcher.addItem("German")

        self.layout.addWidget(self.lang_switcher)

        self.setLayout(self.layout)
