# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Усложнение: * Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=1, flag=0):
    jokes = []
    if flag == 0:
        for i in range(0, n):
            string = (
                f'{(nouns[randint(0, len(nouns) - 1)])} {(adverbs[randint(0, len(adverbs) - 1)])} '
                f'{(adjectives[randint(0, len(adjectives) - 1)])}'
            )
            jokes.append(string)
    else:
        nouns_copy = nouns.copy()
        adverbs_copy = adverbs.copy()
        adjectives_copy = adjectives.copy()
        for i in range(0, n):
            jokes_joke = [
                f'{nouns_copy.pop(randint(0, len(nouns_copy) - 1))} '
                f'{adverbs_copy.pop(randint(0, len(adverbs_copy) - 1))} '
                f'{adjectives_copy.pop(randint(0, len(adjectives_copy) - 1))}'
            ]
            jokes.append(jokes_joke)
    print(jokes)


get_jokes(3, 0)

# Если начения flag != 0, то значение n не должно превышать количество слов в списках (n <= 5), иначе
# будет ошибка.
