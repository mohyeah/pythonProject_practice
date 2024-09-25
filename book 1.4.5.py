'''
牛顿迭代法近似求平方根
'''
def squareroot(n):
    root = n / 2 # initial guess is n/2
    for k in range(20):
        root = (1/2)*(root + (n/root))
    return root
ans = squareroot(10)
print(ans)