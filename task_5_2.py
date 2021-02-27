# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор. Например:
# gen1 = iterator_with_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
#
# Усложнение(**):
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.
# Например:
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

def iterator_with_yield(n=10):
    previous = 0
    for i in [i for i in range(n + 1) if i % 2 and i ** 2 < 200]:
        yield i, previous + i
        previous += i


if __name__ == '__main__':

    gen1 = iterator_with_yield(15)

    while True:
        # print(next(gen1))
        try:
            print(next(gen1))

        except StopIteration:
            print(f'Генератор "истощен"!')
            break
