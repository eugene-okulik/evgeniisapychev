def decorator(func):
    def wrapper(*args, **kwargs):
        first = kwargs.get('first')
        second = kwargs.get('second')
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            operation = '*'
        result = func(first=first, second=second, operation=operation)
        print(result)
    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first = int(input('Введи любое первое число'))
second = int(input('Введи любое второе число'))


calc(first=first, second=second, operation=None)
