# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

import hashlib

def substring_count(input_string):
    input_string = str(input_string).lower()
    hash_set = set()
    word = hashlib.sha1(input_string.encode('utf-8')).hexdigest()
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)+1):
            print(input_string[i:j])
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()

            hash_set.add(h)
    hash_set.discard(word)
    return len(hash_set)


string = 'sova'

print(f'Количество различных подстрок в строке {string}: {substring_count(string)}')