import collections

n= int(input("Введите количество организаций"))
rezult= collections.Counter()
aver=0
for i in range (n):
    kvartal=0
    for z in range(0,4):
        sum = float(input(f"Введите итоги {z+1} квартала для {i} организации"))
        kvartal+=sum
        aver+=sum
    kvartal_eve=kvartal/4
    rezult[i]=kvartal_eve
aver=aver/(n*4)
print(rezult)
for keys, values in rezult.items():
    if values > aver:
        print(f"больше среднего организация № {keys} ")
    if values == aver:
        print(f"Cредния прибыль у организация № {keys} ")
    if values < aver:
        print(f"меньше среднего организация № {keys} ")


