import random

RED_BALLS = [i for i in range(1, 35)]
BLUE_BALLS = [i for i in range(1, 12)]

class bonus:
    def __init__(self, red_ball_num, blue_ball_num,):
        self.red_ball_num = red_ball_num
        self.blue_ball_num = blue_ball_num
    def __repr__(self):
        r = ''
        b = ''
        rdb = random.sample(RED_BALLS, self.red_ball_num)
        rdb.sort()
        for ball in rdb:
            r += f'\033[031m{ball:0>2d}\033[0m '
        bdb = random.sample(BLUE_BALLS, self.blue_ball_num)
        bdb.sort()
        for ball in bdb:
            b += f'\033[034m{ball:0>2d}\033[0m '
        balls = r + b
        return balls

chose = bonus(5, 2)
print(chose)