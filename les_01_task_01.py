number = int(input("Введи число из 3 знаков"))
num1 = number // 100
num2 = number % 100 // 10
num3 = number % 10
sum = num1 + num2 + num3
proizvedenie = num1 * num2 * num3
print("Сумма " + str(sum), "Произведение " + str(proizvedenie))
