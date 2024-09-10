import operator

def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

def calc2(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

print(calc(1, 2, 1.1, Us=2, cNS=3.2))
print(calc2(2, operator.mul, 1, 2, 3, 4, 5))
