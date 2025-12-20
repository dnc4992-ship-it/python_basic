# ch10ex1_단어번역.py

# {} 딕셔너리
# 순서X, 키로 값을구분
# {키 : 값,......}

w = {'apple':'사과','grape':'포도', 'python':'파이썬'}
print(w)

print(w['apple'])

e = input('영어단어?')

if e in w:
    print(w[e]) # 딕셔너리[키] -> 값

else:
    print('사전에 단어가 없습니다.')
     
