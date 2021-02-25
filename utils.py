from requests import get, utils
from decimal import Decimal


def currency_rates(*args):
    def course():
        return Decimal('.'.join(val[1][1: -2].split(',')))
    val_lst = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT', 'CAD',
               'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK',
               'CHF', 'ZAR', 'KRW', 'JPY']

    for i in args:
        if str(i).upper() not in val_lst:
            return None

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # Можно сделать проверку и при ответе != <Response [200]>
    encodings = utils.get_encoding_from_headers(response.headers)  # вывести сообщение напр. "Нет ответа от сервера.
    content = response.content.decode(encoding=encodings).lower()  # Проверьте подключение к интеренету".
    # print(response)
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


if __name__ == "__main__":
    print(currency_rates('GBp'))
