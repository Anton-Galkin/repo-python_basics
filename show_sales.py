import csv
from sys import argv


with open('bakery.csv', encoding='UTF-8', mode='rt') as file:
    file_reader = csv.reader(file, delimiter=',')

    if len(argv) == 1:
        for i in file_reader:
            print(i[0])

    elif len(argv) == 2:
        for i in [row[0] for row in file_reader][int(argv[1]) - 1:]:
            print(i)

        # for i in file_reader:
        #     lst.append(i[0])
        # for i in lst[int(argv[1]) - 1:]:
        #     print(i)

    else:
        for i in [row[0] for row in file_reader][int(argv[1]) - 1:int(argv[2])]:
            print(i)

        # for i in file_reader:
        #     lst.append(i[0])
        # for i in lst[int(argv[1]) - 1: int(argv[2])]:
        #     print(i)
