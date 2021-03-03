# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.


file = open('nginx_logs.txt', encoding='UTF-8', mode='rt')

result = []

for line in file:
    # print(line.strip())
    remote_addr = line[: line.find(' ')]  # Получаем IP адрес из строки
    # print(remote_addr)

    request_type_start = line[line.find('"') + 1:]
    request_type = request_type_start[: request_type_start.find(' ')]  # Получаем тип запроса из строки
    # print(request_type)

    requested_resource_start = request_type_start[request_type_start.find('/') + 1:]
    requested_resource = requested_resource_start[: requested_resource_start.find(' ')]   # Получаем ресурс из строки
    # print(requested_resource)

    answer = (remote_addr, request_type, requested_resource)
    result.append(answer)

file.close()

print(result)
