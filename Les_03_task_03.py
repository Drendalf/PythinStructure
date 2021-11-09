# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]
print(mass)

max = mass[0]
min = mass[0]

for i in mass:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = mass.index(min)
max_index = mass.index(max)
mass[min_index], mass[max_index] = mass[max_index], mass[min_index]
print(mass)