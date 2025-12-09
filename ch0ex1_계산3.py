# ch0ex1_계산2.py

import random

def makequiz(start=1, end=9):
    n1 = random.randint(start, end) #4
    #print(n1)
    n2 = random. randint(start, end) #7
    #print(n2)
    op = random. randint(1, 3) #1 +, 2-, 3*

    if op == 1:
        ops = '+'
    elif op == 2:
        ops = '-'
        # 앞 수가 작으면 두 수 바꾸기
        if n1 < n2:
            n1, n2 = n2, n1
            #t = n1
            #n1 =n2
            #n2 = t
            print('두 수 교체')
            
    else :
        ops = '*'            
    q = f'{n1} {ops} {n2}'  # '4 + 7'
    return q

sc1 = 0
sc2 = 0
no = 5
input('준비되면 엔터를 누르세요!')
start = time.time()
for n in range(1, no + 1) :
    q = makequiz(1, 9)
    a = eval(q)         # eval('1 + 3') -->4
    # print(q, a)
    print(f'문제 {n}.')
    u = int(input(f'{q} = '))
    if u == a:
        sc1 = sc1 + 1
        print('정답!')
    else:
        print(f'오답! 정답은{a}')
        sc2 = sc2 + 1
    print()

end = time.time()
et = end - start

print('-' * 20)
print(f'정답: {sc1}개')
print(f'오답: {sc2}개')
print(f'풀이시간:{et:.1f}초')

if sc2 == 0:
    print(f'모두 정답입니다!.')
if sc2 == 0 and et < 10 :
    print(f'당신은 계산의 신!')
    
