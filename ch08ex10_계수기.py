# ch08ex10_계수기.py

def count():
    global cnt      # cnt는 전역변수
    cnt = cnt + 1
    print(f'{cnt}회 실행')

cnt = 0
count()
count()
count()
