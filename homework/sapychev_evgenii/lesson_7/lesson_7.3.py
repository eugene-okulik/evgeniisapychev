a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'
def func(numb):
    for numb in my_list:
        print(int(numb[numb.index(": "):].replace(': ', '')) + 10)
my_list = [a,b,c,d]
func(my_list)