# Функция для потребления входных данных
shift = lambda inp: bool(inp) and (inp[0], inp[1:])

# Функция, не потребляющая входных данных
nothing = lambda inp: (None, inp)

# Фильтрация по предикату
filt = lambda pred: lambda parser: lambda inp: (res:=parser(inp)) and pred(res[0]) and res

# Соответствие литералу
literal = lambda val: filt(lambda x: x == val)

# Один из множества значений
member = lambda vals: filt(lambda x: x in vals)

# Соответствие отдельному литералу
atom = lambda val: literal(val)(shift)

# Соответствие одному из символов
one_of = lambda vals: member(vals)(shift)

# Применение функции к результату парсера
fmap = lambda func: lambda parser: lambda inp: (res:=parser(inp)) and (func(res[0]), res[1])

# Один или больше (+)
def one_or_more(parser):
    def parse(inp):
        result = []
        while (res:=parser(inp)):
            value, inp = res
            result.append(value)
        return bool(result) and (result, inp)
    return parse

# Несколько парсеров подряд
def seq(*parsers):
    def parse(inp):
        result = []
        for parser in parsers:
            res = parser(inp)
            if not res:
                return False
            value, inp = res
            result.append(value)
        return result, inp
    return parse

# Выбор i-го результата парсера
select = lambda i: fmap(lambda x: x[i])

# Выбор из множества парсеров
select_from = lambda *parsers: lambda i: select(i)(seq(*parsers))

# Выбор результата левого или правого парсера
left = lambda p1, p2: select_from(p1, p2)(0)
right = lambda p1, p2: select_from(p1, p2)(1)

# Выбор одного из парсеров
either = lambda p1, p2: lambda inp: p1(inp) or p2(inp)

# Или парсер, или вернуть значение по умолчанию
maybe = lambda parser: lambda _none: either(parser, fmap(lambda _: _none)(nothing))

# Ноль или больше
zero_or_more = lambda parser: either(one_or_more(parser), seq())

# Выбор первого подошедшего парсера
def choice(*parsers):
    def parse(inp):
        for parser in parsers:
            res = parser(inp)
            if res:
                return res
        return False
    return parse

# Выбор результата между двумя парсерами
between = lambda p1, p2, p3: right(p1, left(p2, p3))