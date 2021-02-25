# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#
# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

from requests import get, utils
from decimal import Decimal


def currency_rates(*args):
    def course():
        return Decimal('.'.join(val[1][1: -2].split(',')))

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # Можно сделать проверку и при ответе != <Response [200]>
    encodings = utils.get_encoding_from_headers(response.headers)  # вывести сообщение напр. "Нет ответа от сервера.
    content = response.content.decode(encoding=encodings).lower()  # Проверьте подключение к интеренету".
    print(response)
    data_start = content.find('date="'.lower())  # дата удобно получается из самого списка,
    data_end = content.find('" ', data_start)    # можно обойтись и без модуля datetime
    data_str = content[data_start + 6: data_end]

    answer = ''

    for i in args:

        str_start = content.find(str(i).lower())
        str_end = content.find('valute', str_start)
        slice_content = content[str_start: str_end]
        val = slice_content.split('value')
        name_val = slice_content.split('name')
        name_val_str = name_val[1][1: name_val[1].find('</')].capitalize()

        nominal_start = slice_content.split('nominal')
        nominal = Decimal(nominal_start[1][1: nominal_start[1].find('</')])

        answer += f'{nominal} {name_val_str} на {data_str} составляет {course().quantize(Decimal("1.00"))} руб.\n'

    return answer


print(currency_rates('hkd', 'kzt'))
