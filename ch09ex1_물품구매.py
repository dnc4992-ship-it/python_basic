# ch09ex1_물품구매.py
# append, insert, remove -리스트에서만 사용할 수 있는 함수(매써드)

cart = []   # 빈 리스트

cart.append('사과')   #리스트.append(데이터)
cart.append('수박')
print(f'cart: {cart}')

cart2 =['홈런볼', '우유']
cart = cart + cart2
print(f'cart: {cart}')

# cart에 2번째 원소를 '멜론'으로 변경
cart[1] = '멜론'
print(f'cart: {cart}')

#cart 3번째 원소 제거
del cart[2]
print(f'cart: {cart}')

# cart에 3번째 '요거트' 추가
cart.insert(2, '요거트')
print(f'cart: {cart}')

# cart에서 '요거트' 제거
cart.remove('요거트')
print(f'cart:{cart}')

# cart에서 '멜론' 인덱스 찾기

index_melon = cart.index('멜론')
print(index_melon)
print(cart[index_melon:])
