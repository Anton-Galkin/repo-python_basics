# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Выводит или не выводить первый элемент - решите сами. Используйте генераторы или генераторные выражения.
#
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# result = [i[1] for i in enumerate(src) if i[1] > src[i[0] - 1]][1:]  # Решение в одну строку

result = []


def iterator():
    previous = src[0]
    for i in [i for i in src]:
        if previous < i:
            result.append(i)
            yield i
        previous = i


if __name__ == '__main__':

    gen = iterator()
    print(gen)

    while True:
        try:
            next(gen)
        except StopIteration:
            break

print(result)
