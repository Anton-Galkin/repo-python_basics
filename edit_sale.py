from sys import argv

# with open('bakery_2.csv', encoding='UTF-8', mode='r+t') as file:
#     lines = file.readlines() #  Происходит загрузка строк файла в список, что противоречит условию задания
#     if int(argv[1]) <= len(file.readlines()):
#         lines[int(argv[1])] = argv[2] + '\n'
#         file.seek(0)
#         file.writelines(lines)
#     else:
#         print(f'Такой записи не существует')

# Решение задачи с помощью создания дополнительного файла и при соблюдении условия,
# что строка с данными есть, перезаписи основного. Толко не могу понять загружается ли файл целиком
# при использовании функции len(file.readlines())?

with open('bakery.csv', encoding='UTF-8', mode='r+t') as file, \
     open('bakery.tmp', encoding='UTF-8', mode='w+t') as temp:

    if int(argv[1]) <= len(file.readlines()):
        file.seek(0)
        for idx, line in enumerate(file):
            if idx == int(argv[1]) - 1:
                temp.write(argv[2] + '\n')
            else:
                temp.write(line)
        file.seek(0)
        temp.seek(0)
        file.write(temp.read())
    else:
        print(f'Такой записи не существует')

# Была попытка обойтись без метода .readlines(), но информация во временный файл записывается правильно,
# а при перезаписи в основной файл происходит что-то непонятное. Так и не смог разобраться.

# with open('bakery.csv', encoding='UTF-8', mode='r+t') as file, \
#         open('bakery.tmp', encoding='UTF-8', mode='w+t') as temp:
#     i = 1
#     for idx, line in enumerate(file):
#         if idx == int(argv[1]) - 1:
#             temp.write(argv[2] + '\n')
#         else:
#             temp.write(line)
#         i += 1
#     if int(argv[1]) > i:
#         print(f'Такой записи не существует')
#     else:
#         file.seek(0)
#         temp.seek(0)
#         file.write(temp.read())
