from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
)


class Timetable(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(headline := QLabel("timetable"))
        headline.setObjectName("headline") # stylesheet link

        self.table = QTableWidget(10, 6, self)

        self.table.setItem(0, 1, QTableWidgetItem("Monday"))
        self.table.setItem(0, 2, QTableWidgetItem("Tuesday"))
        self.table.setItem(0, 3, QTableWidgetItem("Wednesday"))
        self.table.setItem(0, 4, QTableWidgetItem("Thursday"))
        self.table.setItem(0, 5, QTableWidgetItem("Friday"))

        self.layout.addWidget(self.table)

        self.button = QPushButton("back to main menu")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
