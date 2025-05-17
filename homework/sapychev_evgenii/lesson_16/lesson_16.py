import os
import csv
from pathlib import Path
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)


def find_csv_file(filename="data.csv", folder_name=("hw_data")):
    drives = ["C:/", "D:/"] if os.name == 'nt' else ["/"]
    for drive in drives:
        for root, dirs, files in os.walk(drive):
            if folder_name in dirs:
                file_path = Path(root) / folder_name / filename
                if file_path.exists():
                    return file_path


def read_csv_data(csv_path):
    """Reads CSV file using your specified processing"""
    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))
    print(csv_file)


def get_sql_qury():
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT name, second_name, g.title as group_title, b.title as book_title,
                    s2.title as subject_title, l.title as lesson_title, m.value as mark_value
                    from students  as s
                    join `groups` as g  on s.group_id = g.id
                    join books as b on s.id = b.taken_by_student_id
                    join marks as m on s.id  = m.student_id
                    JOIN lessons as l on m.lesson_id = l.id
                    join subjets as s2 on l.subject_id = s2.id''')
    data = cursor.fetchall()
    return data


csv_path = find_csv_file()
csv_data = read_csv_data(csv_path)
sql_qury = get_sql_qury()

common_items = [item for item in csv_data if item not in sql_qury]
print("Отличия", common_items)
db.close()
