# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random
import sys

SIZE_1 = 10


MIN_ITEM = 0
MAX_ITEM = 50

# mass_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_1)]
mass_1 = [41, 32, 11, 36, 1, 25, 21, 8, 5, 26]
print(mass_1)
# Обьем памяти при постановки условия задачи
mem_element= sys.getsizeof(mass_1)
for el in mass_1:
    mem_element+=sys.getsizeof(mem_element)


def func1(mass):
    rezult = []
    for i in mass:
        if i % 2 == 0:
            rezult.append(mass.index(i))
    mem_1 = sys.getsizeof(rezult)
    for el in rezult:
        mem_1 += sys.getsizeof(mem_1)
    return rezult, mem_1


def func2(mass):
    rezult = [i for i in range(len(mass)) if mass[i]%2==0]
    mem_1 = sys.getsizeof(rezult)
    for el in rezult:
        mem_1 += sys.getsizeof(mem_1)
    return rezult, mem_1


def func3(mass):
    rezult = []
    mass_even_number= [i for i in range(0,51,2)]
    for number in mass:
        if number in mass_even_number:
            rezult.append(mass.index(number))
    mem_1 = sys.getsizeof(rezult)
    for el in rezult:
        mem_1 += sys.getsizeof(mem_1)
    for el in mass_even_number:
        mem_1 += sys.getsizeof(mem_1)
    return rezult, mem_1

print(f'количество памяти используемое в работе функцией 1  {func1(mass_1)[1]}')
print(f'количество памяти используемое в работе функцией 2  {func2(mass_1)[1]}')
print(f'количество памяти используемое в работе функцией 3  {func3(mass_1)[1]}')