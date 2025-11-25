# ch07ex3_숫자맞히기.py

import random

com = random.randint(1, 100)
cnt = 0

print('컴퓨터가 생각한 숫자(1~100)를 맞혀보세요.')
print(com)

while True:
    user = int(input('당신의 선택은?'))
    cnt = cnt +1
    if user > com:
        print('입력한 수가 큽니다. 더 작은 숫자를 입력해 보세요.')
    elif user < com:
        print('입력한 수가 작아요. 더 큰 숫자를 입력해 보세요.')
    else:
        break
    
print(f'{cnt}회 출력')
print('성공!!')
