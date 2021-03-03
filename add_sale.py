import csv
from sys import argv


with open('bakery.csv', encoding='UTF-8', mode='at') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
    file_writer.writerow(argv[1:])
