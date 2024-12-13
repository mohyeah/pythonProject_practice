import random

def lcm(x:int, y:int) -> int:
    return x * y // gcd(x, y)

def gcd(x: int, y: int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x

# print(lcm(24, 12))
# print(gcd(24, 12))

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]

def choose():
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls

def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n = int(input('display:'))
for _ in range(n):
    display(choose())

