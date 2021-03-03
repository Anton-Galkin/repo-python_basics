# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# то для оставшихся ФИО значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

import json
from sys import exit
from itertools import zip_longest

with open('users.csv', encoding='UTF-8', mode='rt') as users_file:
    users = [line.replace(',', '').strip() for line in users_file]

with open('hobby.csv', encoding='UTF-8', mode='rt') as hobby_file:
    hobbys = [line.strip() for line in hobby_file]

if len(users) >= len(hobbys):
    users_dic = {user: hobby for user, hobby in zip_longest(users, hobbys)}
    # print(users_dic)
else:
    users_dic = {user: hobby for user, hobby in zip(users, hobbys)}
    # print(users_dic)
    exit(1)

with open('users_dit.json', encoding='UTF-8', mode='wt') as users_dic_file:
    users_dic_file.write(json.dumps(users_dic, indent=4, ensure_ascii=False))

with open('users_dit.json', encoding='UTF-8', mode='rt') as users_dic_file:
    users_dic_read = json.loads(users_dic_file.read())

print(users_dic_read)
