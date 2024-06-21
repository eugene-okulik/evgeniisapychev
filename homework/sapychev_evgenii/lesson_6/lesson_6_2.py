for x in range(1, 101):
    if x // 5 == x / 5: 
        if x // 3 == x / 3: 
            x = 'FuzBuzz'
        else: 
            x = 'Buzz' 
    else:
        if x // 3 == x / 3:
            x = 'Fuzz'
    print(x, end=' ')
