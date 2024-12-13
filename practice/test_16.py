# 计算C(M, N)
'''
def fac(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


m = int(input("Enter the m: "))
n = int(input("Enter the n: "))
print(fac(m) // fac(n) // fac(m - n))
'''
from math import factorial as f

m = int(input("Enter the m: "))
n = int(input("Enter the n: "))
print(f(m) // f(n) // f(m - n))
