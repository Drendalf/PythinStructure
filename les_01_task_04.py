import random
a= int(input("Введите первое число"))
b= int(input("Введите второе число"))
c= random.randint(a,b)
print(c)

a= float(input("Введите первое вещественное число"))
b= float(input("Введите второе вещественное число"))
c= round(random.uniform(a,b), 2)
print(c)

a= ord(input("Введите первую букву"))
b= ord(input("Введите вторую букву"))
c= random.randint(a,b)
print(chr(c))


