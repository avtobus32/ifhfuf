# ------------------------------------------------------------------------------------------------------------------------- #
# проверка на одинаковые цифры в числе: ----------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------- #
a = input('Введите любое число:\n') # запрос числа от пользователя
b = set(a) # перенос числа пользователя в множество b по символам
if len(a) == len(b): # сравнение кол-ва символов в изначальном числе и множестве b
    print('Одинаковые числа не найдены.')
else:
    print('Одинаковые числа найдены!')

# ------------------------------------------------------------------------------------------------------------------------- #
# 
# ------------------------------------------------------------------------------------------------------------------------- #
