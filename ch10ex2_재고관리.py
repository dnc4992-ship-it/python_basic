# ch10ex2_재고관리.py

product = {"펜": 10, "지우개": 5, "노트": 10}

while True:
    name = input("재고 물품명: ")
    if name == 'end':
        break
    if name in product:
        print("이미 있는 물품입니다.")
        
    else:
        cnt = int(input("재고 수량: "))
        product[name] = cnt

    print(product)
    
  
print('-' * 10)
print("물품: ", product.keys())
print("수량: ", product.values())
print('-' * 30)

# 전체딕셔너리 보기
for k, v in product.items():
    print(f'{k}:{v}개')

