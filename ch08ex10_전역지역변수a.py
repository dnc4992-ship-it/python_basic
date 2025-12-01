# ch08ex10_전역지역변수.py

def func():
    x = 5 #지역변수
    c =3

    print(f'func x: {x}')
    print(f'func c: {c}')
    print(f'y: {y}')

x = 10 #  전역변수
y = 5
func()
print(f'x: {x}')
#print(f'c:{c}')
