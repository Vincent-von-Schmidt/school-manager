import psycopg2
import tabulate

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
		JOIN times ON timetable.hour = times.hour
		JOIN subject ON curs.subject = subject.id
		JOIN room ON curs.room = room.id
		JOIN teacher ON curs.teacher = teacher.id
WHERE timetable.semester = 1
ORDER BY timetable.id ASC;

""")

print(tabulate.tabulate(cursor.fetchall()))
