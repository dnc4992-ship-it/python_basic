# ch08ex4_삼각형넓이.py

def triangleArea(b, h):
    a = b * h / 2
    return a  # 결과 면적(a)를 반환

a = triangleArea(5, 7)
print(f'넓이: {a}')

b = triangleArea(10, 20) + triangleArea(5, 5)
print(f'두 삼각형 넓이 합: {b}')
