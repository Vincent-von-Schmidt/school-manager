from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
)
import psycopg2

class Timetable(QFrame):
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
            timetable 
                JOIN curs ON timetable.curs = curs.id
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

        # rows -> 34
        # columns -> 6
        self.table = QTableWidget(34, 6, self)

        # set header
        count = 0
        for x in cursor.description:
            self.table.setItem(0, count, QTableWidgetItem(str(x[0])))
            count += 1

        # set content
        # index as cordinates -> fetch_index = y, content_index = x
        # fetch_index + 1 -> 0 = header
        for fetch_index, fetch in enumerate(cursor.fetchall()):
            for content_index, content in enumerate(fetch):
                self.table.setItem(fetch_index + 1, content_index, QTableWidgetItem(str(content)))

        self.layout.addWidget(self.table)

        self.button = QPushButton("back to main menu")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
