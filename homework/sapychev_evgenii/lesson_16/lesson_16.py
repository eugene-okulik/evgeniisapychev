import dotenv
import mysql.connector as mysql
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

# csv
def get_csv_qury(csv_path):
    with open(csv_path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        return list(file_data)
    print(file_data)


# sql
def get_sql_qury():
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT name, second_name, g.title as group_title, b.title as book_title, s2.title as subject_title, l.title as lesson_title, m.value as mark_value
                    from students  as s
                    join `groups` as g  on s.group_id = g.id
                    join books as b on s.id = b.taken_by_student_id
                    join marks as m on s.id  = m.student_id
                    JOIN lessons as l on m.lesson_id = l.id
                    join subjets as s2 on l.subject_id = s2.id''')
    data = cursor.fetchall()
    return data
    

csv_data = get_csv_qury('/Users/esapychev/PyLesson/homework/eugene_okulik/Lesson_16/hw_data/data.csv')
sql_qury = get_sql_qury()

common_items = [item for item in csv_data if item in sql_qury]
print("Совпадающие записи:", common_items)

db.close()