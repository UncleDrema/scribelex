from scribelex import filt, shift, one_or_more, fmap, seq, atom, one_of, zero_or_more, right
import string as python_string

# Цифра
digit = filt(str.isdigit)(shift)

# Цифры
digits = one_or_more(digit)

# Соединение списка символов в строку
joined_string = fmap(lambda x: ''.join(x))

# Число (строкой)
number_str = joined_string(digits)

# Число (целое)
number = fmap(int)(number_str)

# Парсер пустой строки, возвращает пустую строку и не меняет входные данные, если они пустые, иначе False
empty = lambda inp: (inp, inp) if not inp else False

# Соответствие строке
string = lambda val: joined_string(seq(*[atom(x) for x in val]))

# Соответствие строке из символов
string_of = lambda vals: joined_string(one_or_more(one_of(vals)))

# Строка из букв
string_ascii = string_of(python_string.ascii_letters)

# Строка из печатных символов кроме
string_printable_but = lambda vals: string_of([x for x in python_string.printable if x not in vals])

# Последовательность из хотя бы одного элемента, разделенная разделителем
separated_nonempty_list = lambda parser, separator: \
    fmap(lambda x: [x[0]] + x[1])(seq(parser, zero_or_more(right(separator, parser))))
