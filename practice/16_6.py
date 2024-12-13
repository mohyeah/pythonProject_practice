for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)

def min_fish():
    fish = 1
    while True:
        fish_after_a = fish - fish // 5 - 1
        fish_after_b = fish_after_a - fish_after_a // 5 - 1
        fish_after_c = fish_after_b - fish_after_b // 5 - 1
        fish_after_d = fish_after_c - fish_after_c // 5 - 1
        fish_after_e = fish_after_d - fish_after_d // 5 - 1

        if fish_after_e >= 0:
            return fish
        else:
            fish += 1

print(min_fish())