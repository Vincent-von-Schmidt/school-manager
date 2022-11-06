from PyQt6.QtWidgets import (
    QFrame,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCheckBox
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from src.widgets.div.div import Div


class Dashboard(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout: QVBoxLayout = QVBoxLayout(self)

        button: QPushButton = QPushButton("Div-style-test-button")
        button.setObjectName("div")
        button_layout: QHBoxLayout = QHBoxLayout(button)
        icon1: QLabel = QLabel()
        icon1.setObjectName("icon")
        icon1.setPixmap(QPixmap("assets/home.ico").scaled(
            40, 40,
            Qt.AspectRatioMode.KeepAspectRatio
        ))
        icon2: QLabel = QLabel()
        icon1.setObjectName("icon")
        icon2.setPixmap(QPixmap("assets/settings.ico").scaled(
            40, 40,
            Qt.AspectRatioMode.KeepAspectRatio
        ))
        button_layout.addWidget(icon1)
        button_layout.addWidget(QLabel("Div_style_test_button"))
        button_layout.addWidget(icon2)
        button.setLayout(button_layout)
        self.layout.addWidget(button)

        div_test: QFrame = QFrame(self)
        div_test.setObjectName("div")
        div_test_layout: QHBoxLayout = QHBoxLayout(div_test)
        div_test_layout.addWidget(QLabel("test1"))
        div_test_layout.addWidget(QCheckBox(div_test))
        div_test.setLayout(div_test_layout)
        self.layout.addWidget(div_test)

        div_button_test: QFrame = QFrame(self)
        div_button_test.setObjectName("div")
        div_button_test_layout: QHBoxLayout = QHBoxLayout(div_button_test)
        div_button_test_layout.addWidget(QPushButton("test1"))
        div_button_test_layout.addWidget(QPushButton("test2"))
        div_button_test.setLayout(div_button_test_layout)
        self.layout.addWidget(div_button_test)

        """
        self.layout.addWidget(div_test := Div())
        div_test.addWidget(QLabel("test"))
        div_test.addWidget(QCheckBox(div_test))
        """

        self.setLayout(self.layout)
