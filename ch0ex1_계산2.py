# ch0ex1_계산2.py

import random

def makequiz(start=1, end=9):
    n1 = random.randint(start, end) #4
    print(n1)
    n2 = random. randint(start, end) #7
    print(n2)
    op = random. randint(1, 3) #1 +, 2-, 3*

    if op == 1:
        ops = '+'
    elif op == 2:
        ops = '-'
    else :
        ops = '*'            
    q = f'{n1} {ops} {n2}'  # '4 + 7'
    return q


for n in range(5) :
    q = makequiz(1, 5)
    a = eval(q)         # eval('1 + 3') -->4
    # print(q, a)
    u = int(input(f'{q} = '))
    if u == a:
        print('정답!')
    else:
        print(f'오답! 정답은{a}')
    print()
