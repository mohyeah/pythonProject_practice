tp = ('hello', )
print(type(tp))
a = 1, 10, 100
i, j, l, *m = a
print(i, j, l, m)
print()
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)