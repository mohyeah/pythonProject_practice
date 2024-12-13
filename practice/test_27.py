from datetime import time
import time
from functools import lru_cache

def record_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'execution time: {end - start:.2f} seconds')
        return result
    return wrapper

def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

@lru_cache(maxsize=None)
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

for i in range(1, 51):
    print(fib1(i))