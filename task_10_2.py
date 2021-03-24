# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def sum_cloth(self):
        result = (self.parameter / 6.5 + 0.5) + (2 * self.parameter + 0.3)
        return f'Всего ткани {result:.3f}'

    @abstractmethod
    def abc_method(self):
        return f'Abstract method'


class Coat(Clothes):

    def sum_cloth(self):
        result = self.parameter / 6.5 + 0.5
        return f'Для пальто нужно {result:.3f} ткани'

    def abc_method(self):
        return f'Abstract method'


class Suit(Clothes):

    def sum_cloth(self):
        result = 2 * self.parameter + 0.3
        return f'Для костюма нужно {result} ткани'

    def abc_method(self):
        return f'Abstract method'


coat = Coat(46)
suit = Suit(170)

print(coat.sum_cloth())
print(coat.sum_cloth)
print(suit.sum_cloth())
print(suit.sum_cloth)

