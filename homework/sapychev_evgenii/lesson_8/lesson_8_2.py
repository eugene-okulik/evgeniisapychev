def progression(limit):
    n = 0
    n1 = 1
    num = 0
    count = 1
    print(limit)
    while count < limit:
        yield num
        num = n1 + n
        n = n1
        n1 = num
        count += 1


count = 1
for number in progression(100001):
    if count == 4:
        print(number)
    elif count == 199:
        print(number)
    elif count == 999:
        print(number)
    elif count == 99999:
        print(number)
        break
    count += 1
