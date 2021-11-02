print("Введите 1 точку ")
x1=float(input("x1"))
y1=float(input("y1"))

print("Введите 2 точку ")
x2=float(input("x2"))
y2=float(input("y2"))

if x1==x2:
    print("Деление на 0")
k=(y1-y2)/(x1-x2)
b=y2-k*x2
print("y= "+str(k)+"*x+"+str(b))