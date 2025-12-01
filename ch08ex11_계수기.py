# ch08ex11_계수기.py

def count():
    global c       # cnt는 전역변수
    c += 1          # c = c +1
    
    print(f'{c}. hello python!')

c = 0
count()
count()
count()
