# Определить, какое число в массиве встречается чаще всего
import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100

mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]

max_index = 0
number = 0
result = {}
for i in mass:
    if mass.count(i) > max_index:
        max_index = mass.count(i)
        number = i
print(f'число {number} встречается {max_index} раз ')
