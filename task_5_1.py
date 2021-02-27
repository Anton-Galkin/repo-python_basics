# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор. Например:
# gen1 = iterator_without_yield(11)
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
# Без использования ключевого слова yield: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.

def iterator_without_yield(n=10):
    return (i for i in range(n + 1) if i % 2 and i ** 2 < 200)


if __name__ == '__main__':
    gen1 = iterator_without_yield(20)

    while True:
        # print(next(gen1))
        try:
            print(next(gen1))
        except StopIteration:
            print(f'Генератор "истощен"!')
            break
