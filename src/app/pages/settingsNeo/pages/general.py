from PyQt6.QtWidgets import (
    QFrame,
    QCheckBox,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from src.widgets.div.div import Div
from src.data import translate, config


class General(QFrame):
    def __init__(self) -> None:
        super().__init__()
        
        self.layout = QVBoxLayout(self)

        self.layout.addWidget(div_debug := Div())
        div_debug.addWidget(QLabel(translate("debug")))

        div_debug.addWidget(check_debug := QCheckBox(self))
        check_debug.setChecked(config["general"]["debug"])
        check_debug.stateChanged.connect(lambda: print("debug"))

        self.button_back = QPushButton(translate("back"))
        self.layout.addWidget(self.button_back)

        self.setLayout(self.layout)
