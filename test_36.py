import math
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

#for a in fibonacci(10):
 #   print(a)

'''完美数'''
def perf(n):
    for i in range(1, n+1):
        num = 0
        for k in range(1, i):
            if i % k == 0:
                num += k
        if num == i:
            print(i)
#perf(10000)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
for i in range(2, 100):
    is_prime(i)
