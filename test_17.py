def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b
'''
a = int(input("Enter the a:"))
b = int(input("Enter the b:"))
c = int(input("Enter the c:"))
print(f'It could {make_judgement(a, b, c)}')
'''
import random
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 7)
    return total
n = 3
print(f"Roll {roll_dice()} scores in {n} times")

def foo(n=1):
    print('test ' * n)
