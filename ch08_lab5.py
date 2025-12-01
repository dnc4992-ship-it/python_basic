# ch08_lab5.py

print('체질량지수(BMI) 구하기')

def bmi(h, w):
    h = h / 100   # cm → m 변환
    m = w / (h ** 2)

    if m < 20:
        r = '저체중'
    elif m < 25:
        r = '정상'
    elif m < 30:
        r = '과체중'
    else:
        r = '비만'
    return m, r

h = int(input('키(cm): '))
w = int(input('몸무게(kg): '))

m, r = bmi(h, w)

print(f'키: {h}cm, 몸무게: {w}kg')
print(f'당신은 과체중(BMI는 {m:.2f}이며, {r})입니다.')
