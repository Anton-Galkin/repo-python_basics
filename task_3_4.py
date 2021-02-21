# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus_adv(*args):
    lst = list(args)
    # print(sorted(lst))
    dic_surname = {}
    lst_sort = []

    for i in lst:
        for l in i.split()[1]:
            if l[0] not in lst_sort:
                lst_sort.append(l[0])
            break

    for k in sorted(lst_sort):
        a = k
        dic_surname[k] = {}
    # print(sorted(lst_sort))

    for k in dic_surname.keys():
        lst_surname = []
        for i in sorted(lst):
            if i.split()[1][0] == k:
                lst_surname.append(i)

        dic_name_str = {i[0]: [] for i in lst_surname}

        for i in dic_name_str.keys():
            lst_name = []
            for j in lst_surname:
                if j[0] == i:
                    lst_name.append(j)
            dic_name_str[i] = lst_name
        dic_surname[k] = dic_name_str

    return dic_surname


print(
    thesaurus_adv('Антон Антонов', 'Алина Егорова', 'Анастасия Ерёмина', 'Ольга Алексеева', 'Евгений Савин',
                  'Олег Финогин', 'Егор Яковлев',
                  'Анна Фомина', 'Яков Борисов', 'Борис Яковлев', 'Александр Анохин'))
