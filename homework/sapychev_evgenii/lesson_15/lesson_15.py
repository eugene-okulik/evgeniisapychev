import mysql.connector as mysql


db = mysql.connect(
    user = 'st-onl',
    passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    database = 'st4'
)


cursor = db.cursor()
cursor.execute('INSERT INTO students (name, second_name) VALUES (%s, %s)', ('Sapychev', 'Probiu'))
id_user = cursor.lastrowid
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('book_int', id_user))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('book2_str', id_user))
cursor.execute("INSERT INTO `groups`  (title, start_date, end_date) VALUES (%s, %s, %s)", ('1', '2', '3'))
id_groups = cursor.lastrowid
cursor.execute("UPDATE students s set group_id = %s where s.id = %s", (id_groups, id_user))
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ('sub13',))
id_lesson_1 = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ('sub23',))
id_lesson_2 = cursor.lastrowid
calendar = [('сегодня', id_lesson_1), ('вчера', id_lesson_1), ('завтра', id_lesson_2), ('послезавтра', id_lesson_2)]
lesson_id = []
for title, subject_id in calendar:
    cursor.execute("INSERT into lessons (title, subject_id ) VALUES (%s, %s)", (title, subject_id))
    lesson_id.append(cursor.lastrowid)
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (2, lesson_id[0], id_user))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (3, lesson_id[1], id_user))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (4, lesson_id[2], id_user))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (5, lesson_id[3], id_user))
s2 = cursor.execute("SELECT value FROM marks WHERE student_id = %s", (id_user,))
all_marks = cursor.fetchall()
s1 = cursor.execute("SELECT title FROM books WHERE taken_by_student_id  = %s", (id_user,))
all_books = cursor.fetchall()
s3 = cursor.execute('''SELECT * 
from students s2
JOIN st4.marks m on s2.id = m.student_id
JOIN st4.books b on s2.id = b.taken_by_student_id 
JOIN st4.lessons l  on l.id  = m.lesson_id 
JOIN st4.subjets s on s.id = l.subject_id
where s2.id = %s''', (id_user,))
last_req = cursor.fetchall()
db.commit()
print(all_marks)
print(all_books)
print(last_req)
db.close()