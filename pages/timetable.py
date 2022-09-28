from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
)
import psycopg2

class Timetable(QWidget):
    def __init__(self) -> None:
        super().__init__()

        connection = psycopg2.connect(
            host="192.168.178.23",
            port="5400",
            database="school",
            user="postgres",
            password="delta1"
        )

        cursor = connection.cursor()

        cursor.execute("""

        SELECT 
            day.name AS day,
            timetable.hour,
            curs.name AS curs_id,
            subject.name AS subject,
            room.name as room,
            FORMAT('%s, %s', teacher.last_name, teacher.first_name) AS teacher
        FROM
            timetable JOIN curs ON timetable.curs = curs.id
                JOIN day ON timetable.day = day.id
                JOIN subject ON curs.subject = subject.id
                JOIN room ON curs.room = room.id
                JOIN teacher ON curs.teacher = teacher.id
        WHERE timetable.semester = 1
        ORDER BY timetable.id ASC;

        """)

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(headline := QLabel("timetable"))
        headline.setObjectName("headline") # css ident

        self.table = QTableWidget(10, 7, self)

        count = 1
        for x in cursor.description:
            self.table.setItem(0, count, QTableWidgetItem(x[0]))
            count += 1

        self.layout.addWidget(self.table)

        self.button = QPushButton("back to main menu")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
