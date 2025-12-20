# ch09_lab6a.py

import random

# 1~6

num = []
cnt = 0
while cnt < 6 :
    n = random.randint(1, 6)
    # n이 num 리스트에 없다면 추가
    if n not in num :
        num.append(n)
        cnt = cnt +1
        print(f'{n} 추가')

    else:
        print(f'{n} 중복으로 폐기')

print(num)
