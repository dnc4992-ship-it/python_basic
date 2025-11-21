# ch06_lab5(연습).py


a = int(input(f'첫번째 정수(a)를 입력하세요 : '))

b = int(input(f'두번째 정수(b)를 입력하세요 : '))


print('홀수들:  ', end =' ')   # 인쇄될때 옆으로 숫자가 오도록 





for n in range (a, b+1 ) :

    if n % 2 == 1:   # 홀수

       print(n, end=' ')
