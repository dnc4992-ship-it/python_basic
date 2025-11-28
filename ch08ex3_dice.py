# ch08ex3_dice.py

import random
def dice():
    return random.randint(1,6)

d1 = dice()
d2 = dice()
print(f'1번 주사위 눈금: {d1}')
print(f'2번 주사위 눈금: {d2}')
