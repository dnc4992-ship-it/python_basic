# ch04_lab6.py


print('일일 판매량을 입력하세요.')

print()


americano = int(input('아메리카노 판매 수:  :') )                           # 1일 판매 : 아메리카노 20



cafe_ratte = int(input('카페라떼 판매 수:  :') )                                 # 1일 판매 : 카페라떼 10



bannillra_ratte = int(input('바닐라라떼 판매 수:  :'))                           # 1일 판매 : 바닐라라떼 15



total = (americano * 2000) + (cafe_ratte * 3000) + (bannillra_ratte * 3500)      # 3종류의 커피 1일 판매액

    
print(f"일일 판매 매출액은 {total} 입니다.")                                     # 일일 판매합계



print()

month_1= total * 30


print(f"한 달 30일 기준 예상 매출액은 {month_1} 입니다.")                          # 한달(30일)  매출액




expenses = int(input("예상지출액을 입력하세요 :  ")  )                             # 예상지출액 : 2000000


profit = month_1- expenses



print(f"한달 예상 순이익은 {profit}입니다.")



