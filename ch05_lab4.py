# ch05_lab4.py

h = int(input('현재 몇 시 인가요?'))
m = int(input('몇 분인가요?'))




if  m <= 30 :
    h = h-1
    m = m+60

m = m-30

print(f'30분 전은 {h}시 {m}분 입니다.')

