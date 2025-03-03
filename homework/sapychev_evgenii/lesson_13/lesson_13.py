import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
data2_path = os.path.join(base_path, 'data2.txt')


with open(hw_file_path, 'r') as file:
    lines = file.readlines()


processed_lines = []
date_objects = []
for line in lines:
    if ' - ' in line:
        part_before_dash = line.split(' - ')[0]
        date_part = part_before_dash.split('. ', 1)[-1].strip()
        processed_lines.append(date_part + '\n')
        try:
            date_obj = datetime.datetime.strptime(date_part, '%Y-%m-%d %H:%M:%S.%f')
            date_objects.append(date_obj)
        except ValueError as err:
            print('Ошибка')
            raise err


date_objects[0] = date_objects[0] + datetime.timedelta(weeks=1)
date_objects[1] = date_obj.strftime('%A')
date_objects[2] = datetime.datetime.now() - date_objects[2]
date_objects[2] = date_objects[2].days
processed_lines[0] = f"{date_objects[0]}\n"
processed_lines[1] = f"{date_objects[1]}\n"
processed_lines[2] = f"{date_objects[2]} дней"


with open(data2_path, 'w') as file:
    file.writelines(processed_lines)
