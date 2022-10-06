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

cursor.execute("SELECT * FROM times;")
times = cursor.fetchall()

cursor.execute("SELECT day.name FROM day;")
weekdays = cursor.fetchall()

timetable = []

for hour in times:
	timetable.append((hour[0]))

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

print(tabulate.tabulate(fetch := cursor.fetchall(), headers=[x[0] for x in cursor.description], tablefmt="pretty"))
print(fetch)

print(tabulate.tabulate(timetable, headers=[x[0] for x in weekdays], tablefmt="pretty"))
