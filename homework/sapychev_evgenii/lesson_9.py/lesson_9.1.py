import datetime

date = "Jan 15, 2023 - 12:05:33"
pythone_date = datetime.datetime.strptime(date, '%b %d, %Y - %X')
quest_1 = datetime.datetime.strftime(pythone_date, '%B')
quest_2 = datetime.datetime.strftime(pythone_date, '%d.%m.%y, %H:%M')
print(quest_1)
print(quest_2)
