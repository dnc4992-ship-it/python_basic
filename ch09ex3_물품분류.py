#ch09ex3_물품분류.py

cart = ['우유','요거트','라면','과자']

#one : 리스트 원소
pack1 = []
pack2 = []

for one in cart:
    if one in ['우유','요거트']:
        print(f'{one} 유제품, 냉장 포장')
        pack1.append(one)
    else:
        pack2.append(one)
        print(f'{one} 일반포장')

print(f'냉장포장: {pack1}')
print(f'일반포장: {pack2}')
        

            
