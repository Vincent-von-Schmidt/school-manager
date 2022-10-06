from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt
import psycopg2
import data


class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(headline := QLabel(data.translate("timetable")))
        headline.setObjectName("headline") # css ident

        try: 
            connection = psycopg2.connect(
                host=data.config["timetable"]["host"],
                port=data.config["timetable"]["port"],
                database=data.config["timetable"]["database"],
                user=data.config["timetable"]["user"],
                password=data.config["timetable"]["password"]
            )

            cursor = connection.cursor()
            
            cursor.execute("""

            SELECT
                FORMAT('%s. %s - %s', times.hour, times.start_time, times.end_time) AS hour,
                timetable_monday.subject AS monday,
                timetable_tuesday.subject AS tuesday,
                timetable_wednesday.subject AS wednesday,
                timetable_thursday.subject AS thursday,
                timetable_friday.subject AS friday
            FROM
                times
                    LEFT JOIN (
                        SELECT
                            timetable.hour,
                            subject.name AS subject
                        FROM 
                            timetable 
                                JOIN curs ON timetable.curs = curs.id
                                JOIN subject ON curs.subject = subject.id
                        WHERE timetable.semester = 1 AND timetable.day = 1
                            ) AS timetable_monday USING (hour)
                    LEFT JOIN (
                        SELECT 
                            timetable.hour,
                            subject.name AS subject
                        FROM
                            timetable 
                                JOIN curs ON timetable.curs = curs.id
                                JOIN subject ON curs.subject = subject.id
                        WHERE timetable.semester = 1 AND timetable.day = 2
                        ) AS timetable_tuesday USING (hour)
                    LEFT JOIN (
                        SELECT
                            timetable.hour,
                            subject.name AS subject
                        FROM
                            timetable 
                                JOIN curs ON timetable.curs = curs.id
                                JOIN subject ON curs.subject = subject.id
                        WHERE timetable.semester = 1 AND timetable.day = 3
                        ) AS timetable_wednesday USING (hour)
                    LEFT JOIN (
                        SELECT
                            timetable.hour,
                            subject.name AS subject
                        FROM
                            timetable
                                JOIN curs ON timetable.curs = curs.id
                                JOIN subject ON curs.subject = subject.id
                        WHERE timetable.semester = 1 AND timetable.day = 4
                        ) AS timetable_thursday USING (hour)
                    LEFT JOIN (
                        SELECT
                            timetable.hour,
                            subject.name AS subject
                        FROM
                            timetable
                                JOIN curs ON timetable.curs = curs.id
                                JOIN subject ON curs.subject = subject.id
                        WHERE timetable.semester = 1 AND timetable.day = 5
                        ) AS timetable_friday USING (hour)
            WHERE times.hour > 0 AND times.hour < 10;

            """)

            # rows -> 10
            # columns -> 6
            self.table = QTableWidget(10, 6, self)

            # set headers
            # cordinates -> 0 -> y, count -> x
            count = 0
            for x in cursor.description:
                self.table.setItem(0, count, QTableWidgetItem(data.translate(str(x[0]))))
                count += 1

            # set content
            # index as cordinates -> fetch_index = y, content_index = x
            # fetch_index + 1 -> 0 = header
            for fetch_index, fetch in enumerate(cursor.fetchall()):
                for content_index, content in enumerate(fetch):

                    # NULL check
                    if content == None:
                        content = ""
                    
                    self.table.setItem(
                        fetch_index + 1,
                        content_index,
                        item := QTableWidgetItem(data.translate(str(content)))
                    )

                item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable)

            self.table.cellClicked.connect(lambda: print(f"x = {self.table.currentColumn()}; y = {self.table.currentRow()}"))

            self.layout.addWidget(self.table)

        except psycopg2.OperationalError as error:
            self.layout.addWidget(QLabel(str(error)))

        self.button = QPushButton(data.translate("back"))
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
