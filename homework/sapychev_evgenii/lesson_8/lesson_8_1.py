import random

salary = int(input('Какая у тебя зарплата?'))
bonus = bool(random.getrandbits(1))
if bonus is True:
    salary = int(random.random() * 10000) + salary
    print(f'Я готов выдать тебе зарплату с премией, возьми {salary}(True)')
else:
    print('Премии не будет(False)')
