temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29,
                25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temp = list(filter(lambda x: x > 28, temperatures))
print(f'max = {max(hot_temp)}, min = {min(hot_temp)}, avg = {round(sum(hot_temp) / len(hot_temp), 1)}')
