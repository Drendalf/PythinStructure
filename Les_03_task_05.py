# В массиве найти максимальный отрицательный элемент. Вывести на
#  экран его значение и позицию в массиве.

import random

SIZE = 30
MIN_ITEM = -50
MAX_ITEM = 50

mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]
print(mass)
min_index = 0

for i in mass:
    if mass[min_index] > i:
        min_index = mass.index(i)

if mass[min_index] >= 0:
    print(f'нет отрицательных элементов')
else:
    print(f'минимальный отрицательный элемент {mass[min_index]} на {min_index} позиции ')