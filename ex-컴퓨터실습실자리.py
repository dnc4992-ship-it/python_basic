# 컴퓨터실습실자리.py


ex_man = int(input('실습을 참가하겠습니다. 인원은?'))

print()



room = 24       # 방1개  = 실습인원

# 참가자에 필요한 방

need_room = ex_man // room

if ex_man % room > 0 :
    
   need_room += 1

print(f'저희가 필요한 실습실은{need_room}개 입니다.')
