from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt
import psycopg2
import data
from widgets.div import Div

class Timetable(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.vLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)

        self.vLayout.addWidget(headline := QLabel(data.translate("timetable")))
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
            for fetch_index, fetch in enumerate(cursor.fetchall()):
                for content_index, content in enumerate(fetch):

                    # NULL check
                    if content == None:
                        content = ""
                    
                    # fetch_index + 1 -> 0 = header
                    self.table.setItem(
                        fetch_index + 1,
                        content_index,
                        QTableWidgetItem(data.translate(str(content)))
                    )

            if data.debug:
                self.table.cellClicked.connect(
                    lambda: print(
                        f"x = {self.table.currentColumn()}; y = {self.table.currentRow()}"
                    ))

            self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

            self.hLayout.addWidget(self.table, 1)

            self.hLayout.addWidget(info_screen := Div(), 1)

            # infoscreen
            info_screen.addWidget(header := QLabel(data.translate("info")))
            info_screen.addWidget(content := QLabel(""))

            # header
            self.table.cellClicked.connect(lambda: header.setText(
                data.translate(
                    str(self.table.item(0, self.table.currentColumn()).text())
                )
            ))

            cursor.execute("""
            
                SELECT 
                    curs.name AS curs,
                    subject.name AS subject,
                    teacher.last_name AS teacher
                FROM 
                    curs
                        JOIN subject ON curs.subject = subject.id
                        JOIN teacher ON curs.teacher = teacher.id;
            
            """)

            # content
            self.table.cellClicked.connect(lambda: content.setText(
                data.translate(str(cursor.fetchall()))
            ))

        except psycopg2.OperationalError as error:
            # in case connection to database server failed 
            self.hLayout.addWidget(QLabel(str(error)))

        self.vLayout.addLayout(self.hLayout)

        self.button = QPushButton(data.translate("back"))
        self.vLayout.addWidget(self.button)

        self.setLayout(self.vLayout)
