import random as r
answer = r.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('enter a num:'))
    if num < answer:
        print('smaller')
    elif num > answer:
        print('bigger')
    else:
        print('right')
        break
print(f'total try:{counter}')


