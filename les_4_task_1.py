# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random
import timeit
import cProfile
SIZE_1 = 10
SIZE_2=20
SIZE_3=40
SIZE_4=80
SIZE_5=160
SIZE_6=320
SIZE_7=640
SIZE_8=1280
SIZE_9=2560
SIZE_10=5120

MIN_ITEM = 0
MAX_ITEM = 50

mass_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_1)]
mass_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_2)]
mass_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_3)]
mass_4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_4)]
mass_5 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_5)]
mass_6 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_6)]
mass_7 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_7)]
mass_8 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_8)]
mass_9 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_9)]
mass_10 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE_10)]

def func1(mass):
    rezult = []
    for i in mass:
        if i % 2 == 0:
            rezult.append(mass.index(i))
    return rezult


def func2(mass):
    rezult = [i for i in range(len(mass)) if mass[i]%2==0]
    return rezult


def func3(mass):
    rezult = []
    mass_even_number= [i for i in range(0,51,2)]
    for number in mass:
        if number in mass_even_number:
            rezult.append(mass.index(number))
    return rezult

print("-"*25+"func1"+"-"*25)
print(timeit.timeit("func1(mass_1)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_2)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_3)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_4)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_5)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_6)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_7)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_8)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_9)", number=1000, globals=globals()))
print(timeit.timeit("func1(mass_10)", number=1000, globals=globals()))
print(cProfile.run("func1(mass_1)"))
print("-"*25+"func2"+"-"*25)
print(timeit.timeit("func2(mass_1)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_2)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_3)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_4)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_5)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_6)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_7)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_8)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_9)", number=1000, globals=globals()))
print(timeit.timeit("func2(mass_10)", number=1000, globals=globals()))
print(cProfile.run("func2(mass_1)"))
print("-"*25+"func3"+"-"*25)
print(timeit.timeit("func3(mass_1)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_2)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_3)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_4)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_5)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_6)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_7)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_8)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_9)", number=1000, globals=globals()))
print(timeit.timeit("func3(mass_10)", number=1000, globals=globals()))
print(cProfile.run("func3(mass_1)"))

# Вывод. все 3 функции имеют линейную асимптотику при увеличение
# списка в 2 раза время обработки так же увеличивается в 2 раза.
# Эффективнее работает 2 функция это видно из замеров времени а так же  по числу вызовов