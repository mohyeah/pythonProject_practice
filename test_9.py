import random as r
counter = [0] * 6
for _ in range(6000):
    face = r.randrange(1, 7)
    counter[face - 1] += 1
for face in range(1, 7):
    print(f'{face} appear {counter[face - 1]} times')
