# ch09_lab6-2.py

import random

n = []

for i in range(1, 46):
    n.append(i)

print(n)

random.shuffle(n)
print(n)

print(n[:6])
