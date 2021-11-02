first = ord(input("Введите первую букву"))
sec = ord(input("Введите вторую букву"))

first = first - ord("a") + 1
sec = sec - ord("a") + 1
print(f'Порядковый номер првой буквы {first}, второй {sec}, букв между ними = {((first - sec) - 1) * -1}')
