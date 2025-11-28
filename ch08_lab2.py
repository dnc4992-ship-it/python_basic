# ch08_lab2.py

# 함수 정의 : 명령어를 생성
def gugudan(dan) :
    
    for i in range(1, 10) :     #범위내에서 호출

        print(f'{dan}*{i} = {dan * i}')


dan = int(input('단을 입력하세요 : '))

# 함수 호출 : 명령어 실행

gugudan(4)
