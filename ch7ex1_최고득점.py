# ch7ex1_최고득점.py

cnt = 1
mx = 0
mx_no = 0

while True:
    rec = int(input(f'{cnt}회차 득점 : ')) # 입력
    if rec < 0 :        # 입력받은 점수 비교
        break           # 반복 종료
    
    if rec > mx :       # rec >mx 인경우
        mx = rec
        mx_no = cnt
        
        cnt = cnt + 1

if mx == 0 :
    print('기록이 없습니다.')

else:
    print(f'최고 기록은 {mx_no}회차 {mx}점 입니다.')
