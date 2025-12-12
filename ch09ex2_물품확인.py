# ch09ex2_물품확인.py

cart = ['사과', '멜론']
cart2 =['우유', '요거트', '사과']

cart.extend(cart2)  # cart = cart + cart2
print(f'cart: {cart}')

# 원소 개수
cnt = len(cart)
print(f'카트에 물품이 {cnt}개 있다.')

# 특정 원소 개수
cnt_apple =cart.count('사과')
print(f'카트에 사과가{cnt_apple}개 있다.')

# 유제품 추출
new = cart[2:4]
print(f'유제품{new}')

# 원소 확인
item = input('확인할 물품: ')
print(item in cart)
print(item not in cart)

if item in cart:
    print('이미 구매')
else:
    print('구매 전')
  
  



