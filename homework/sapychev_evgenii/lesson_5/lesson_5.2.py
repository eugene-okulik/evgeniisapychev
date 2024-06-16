a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
print(int(a[a.index(": "):].replace(': ','')) + 10)
print(int(b[b.index(": "):].replace(': ','')) + 10)
print(int(c[c.index(": "):].replace(': ','')) + 10)
