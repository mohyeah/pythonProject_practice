# 匿名函数 lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。

import functools
import operator

old_nums = [1, 2, 3, 4, 5]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
# filter 过滤
#print(new_nums)

fac = lambda n: functools.reduce(operator.mul, range(2, n+1), 1)
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

print(fac(6))
print(is_prime(37))

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int2('1001'))