from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QPushButton, QFrame, QCheckBox
)
import src.data as data

class General(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("general"))

        self.layout.addWidget(debug_button := QCheckBox(data.translate("debug")))
        debug_button.setChecked(data.config["general"]["debug"])
        debug_button.stateChanged.connect(lambda: self.set_debug(debug_button.isChecked()))
        
        self.setLayout(self.layout)

    def set_debug(self, state: bool) -> None:
        data.config["general"]["debug"] = state
