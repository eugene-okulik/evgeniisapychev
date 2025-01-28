import random


def decorator(func):
    def wrapper(*args):
        func(*args)
        print('finish')
    return wrapper


@decorator
def example(text):
    print(text)


@decorator
def random_number():
    random_numb = random.randint(0, 9)
    while True:
        while_numb = int(input('Введите число от 0 до 9'))
        if while_numb == random_numb:
            break
        else:
            print('Попробуй еще раз')
            continue
    print('Молодец, угадал')


example('print_me')
random_number()
