#  택시 필요한 대수 계산.py


all_man = int(input('택시를 타야하는 사람이 몇명입니까?'))


# 하나의 택시는 4명이 탈수 있다.

one_taxi = 4


# 입력된 사람에 필요한 택시

call_taxi = all_man // one_taxi     # 필요한 택시수(몫)

if all_man % one_taxi > 0 :

   call_taxi += 1


print(f'택시를 {call_taxi}대 불러주세요')


