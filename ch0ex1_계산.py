# ch0ex1_계산.py

import random

def makequiz(start, end):
    n1 = random.randint(start, end) #4
    print(n1)
    n2 = random. randint(start, end) #7
    print(n2)
    q = f'{n1} + {n2}'  # '4 + 7'
    return q

q = makequiz(20, 90)
print(q)
