# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from sys import argv
from utils import currency_rates as cr


for i in argv[1:]:
    print(cr(i))
