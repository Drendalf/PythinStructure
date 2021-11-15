import timeit
import cProfile


def rez(number):
    count = 1
    curentpos = 2

    while count < number:
        curentpos += 1
        for i in range(2, curentpos):
            if curentpos % i == 0:
                break
            else:
                count += 1
    return curentpos


z_2 = timeit.timeit("rez(2)", number=1000, globals=globals())  #0.0020191850000000067
z_4 = timeit.timeit("rez(4)", number=1000, globals=globals())  # 0.004142786000000009
z_8 = timeit.timeit("rez(8)", number=1000, globals=globals())   # 0.013815236000000009
z_16 = timeit.timeit("rez(16)", number=1000, globals=globals())  # 0.019122678999999976
z_32 = timeit.timeit("rez(32)", number=1000, globals=globals())  # 0.021991928999999993
z_64 = timeit.timeit("rez(64)", number=1000, globals=globals())  # 0.02879691399999998
z_128 = timeit.timeit("rez(128)", number=1000, globals=globals())  # 0.038047678
z_256 = timeit.timeit("rez(256)", number=1000, globals=globals())  # 0.06774865199999996
z_512 = timeit.timeit("rez(512)", number=1000, globals=globals())  # 0.139911397

print(z_2, z_4, z_8, z_16, z_32, z_64, z_128, z_256, z_512, sep= "\n")
print (cProfile.run("rez(512)"))

# функция имеет квадратичную асимптотику