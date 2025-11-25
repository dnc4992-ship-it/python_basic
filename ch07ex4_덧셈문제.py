# ch07ex4_덧셈문제.py

import random
cnt = 0
cnt1 = 0
for i in range(5):
    n1 = random.randint(1,9)
    n2 = random. randint(1,9)
    answer = n1 +n2
    quiz = f'{n1} + {n2} = '
    print(f'{i+ 1}번 문제')
    user = int(input(quiz))
    if user == answer:
        print('정답!')
        cnt = cnt + 1
        
    else:
        print('오답!')
        cnt1 = cnt1 + 1
        
print(f'정답 입력은{cnt}회입니다.')
print(f'오답 입력은{cnt1}회입니다.')
