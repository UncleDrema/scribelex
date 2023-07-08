from scribelex import *

# Цифра
digit = filt(str.isdigit)(shift)

# Цифры
digits = one_or_more(digit)

# Число (строкой)
number_str = fmap(lambda x: ''.join(x))(digits)

# Число (целое)
number = fmap(int)(number_str)

# Парсер пустой строки, возвращает пустую строку и не меняет входные данные, если они пустые, иначе False
empty = lambda inp: (inp, inp) if not inp else False

# Соответствие строке
string = lambda val: fmap(lambda x: ''.join(x))(seq(*[atom(x) for x in val]))