my_dict = {'tuple': ('text', 1, False, 2, True), 'list': [1, 2, 3, 'text', True],
           'dict': {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}, 'set': {1, 2, 3, 'text', False}}
print(my_dict['tuple'][-1])
my_dict['list'].append(100)
my_dict['list'].pop(1)
my_dict['dict'].update({('i am a tuple', ): 'text'})
my_dict['dict'].pop('key1', None)
my_dict['set'].add(257)
my_dict['set'].remove(0)
#print(type['dict'](('i am a tuple', ))) Проверка на тип tuple
print(my_dict)
