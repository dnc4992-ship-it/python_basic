# ch05ex2_덧셈문제.py

n1 = 7
n2 = 3

quiz = f'{n1} + {n2} = '
user = int(input(quiz))
answer = n1 +n2
if user == answer:
    print('정답')
else:
    print('다시 생각해 보세요!')
