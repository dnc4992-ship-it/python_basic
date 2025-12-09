# ch0ex1_계산.py

import random

def makequiz():
    n1 = random.randint(1, 9) #4
    print(n1)
    n2 = random. randint(1,9) #7
    print(n2)
    q = f'{n1} + {n2}'  # '4 + 7'
    return q

q = makequiz()
print(q)
