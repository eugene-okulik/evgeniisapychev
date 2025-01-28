PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
new_list = PRICE_LIST.split()
dict_key = new_list[::2]
dict_value = new_list[1::2]
new_dict = {dict_key: int(dict_value.replace('р', '')) for dict_key, dict_value in zip(dict_key, dict_value)}
print(new_dict)
