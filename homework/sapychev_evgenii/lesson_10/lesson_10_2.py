def main_func(func):
    def repeat_me(*args, **kwargs):
        count = kwargs.pop('count', 1)

        def wrapper():
            for _ in range(count):
                func(*args)
        return wrapper()
    return repeat_me


@main_func
def example(text):
    print(text)


example('print me', count=2)
