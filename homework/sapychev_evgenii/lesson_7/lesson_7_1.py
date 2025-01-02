import random

random_numb = random.randint(0, 9)
while True:
    while_numb = int(input('Введите число от 0 до 9'))
    if while_numb == random_numb:
        break
    else:
        print('Попробуй еще раз')
        continueы

print('Молодец, угадал')
