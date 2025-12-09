# ch0ex1_계산시험.py

import random

def make_quiz(start=1, end=9):
    n1 = random.randint(start, end)
    n2 = random. randint(start, end)
    op = randm. randint(1, 3)
    if op ==1:
        ops = '+'
    elif op ==2:
        ops = '-'
    else:
        ops = '*'
    quiz = f'{n1} {ops} {n2}'
    return quiz

n  = 5
for no in range(1, n+1):
    quiz =make_quiz(10, 20)
    answer = eva1(quiz)
    user = int(input(f'{zuiz}= '))
    if user == answer:
        print('정답')
    else:
        print('오답')
        
