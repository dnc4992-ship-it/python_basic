# ch06ex9_구구단.py



for n in range(2, 10):  # n: 2~9 구구단
    print(f'{n}단========')
    
    for i in range(1, 9 +1):
        print(f'{n} * {i} = {n * i}')
    print()
