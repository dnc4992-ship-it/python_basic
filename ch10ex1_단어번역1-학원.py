# ch10ex1_단어번역1.py

# {} 딕셔너리
# 순서X, 키로 값을구분
# {키 : 값,......}

w = {'apple':'사과','grape':'포도'}
w['python'] = '파이썬'       # 딕셔너리[키] = 값, 딕셔너리에 값 추가하기
w['keyboard']='자판'

print(w)

print(w['apple'])


while True:
    e = input('영어단어?')
    if e =='종료' :
        break

    if e in w:
        print(w[e]) # 딕셔너리[키] -> 값

    else:
        print('사전에 단어가 없습니다.')
        user = input('단어를 추가할까요? (y/n)? ')
        if user == 'y' :
            kr = input('번역할 단어: ')
            w[e] =kr
     
