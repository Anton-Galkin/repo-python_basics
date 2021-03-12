# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def wrapper(*args, **kwargs):
        str = ''
        for i in args:
            str += f'{i}: {type(i)}, '
        for i in kwargs.values():
            str += f'{i}: {type(i)}, '
        return str[0: -2]

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


logger_f = calc_cube(1, 58, x=5, y=654.123, z='qwerty')
print(logger_f)
