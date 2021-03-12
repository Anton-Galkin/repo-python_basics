# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
#
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

data = re.compile(r'''
^([a-z0-9_-]+\.*[a-z0-9_-]+) # username
@
([a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$) # domain
''', re.VERBOSE)


def email_parse(e_mail):
    result = data.search(e_mail)

    if result is None:
        msg = f'wrong email: {e_mail}'
        raise ValueError(msg)

    lst = ['username', 'domain']

    result = {username: domain for username, domain in zip(lst, result.groups())}

    return result


def email_parse_without_compile(e_mail):
    data = re.match(r'^([a-z0-9_-]+\.*[a-z0-9_-]+)@([a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$)', e_mail)

    if data is None:
        msg = f'wrong email: {e_mail}'
        raise ValueError(msg)

    lst = ['username', 'domain']

    res = {username: domain for username, domain in zip(lst, data.groups())}

    return res


e_male = 'a.galkin@mz35.ru'

print(email_parse(e_male))
print(email_parse_without_compile(e_male))
