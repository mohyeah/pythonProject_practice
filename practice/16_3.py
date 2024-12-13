"""
迭代工具模块
"""
import itertools

ls = []
# 产生ABCD的全排列
for i in itertools.permutations('ABCD'):
    ls.append(i)
print(ls)
# 产生ABCDE的五选三组合
for i in itertools.combinations('ABCDE', 3):
    print(i)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))