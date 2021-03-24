# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.


class Matrix:

    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.m_list]))


A = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(A)
