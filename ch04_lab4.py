# ch04_lab4.py

m = int(input('교환할 금액을 입력하세요:'))
print()
change = m  # 교환할 금액을 넣는다
print(f'교환할 금액 : {m}')

cnt50000 = change // 50000  # 50,000원으로 나눈몫.
change = change % 50000

cnt10000 = change // 10000  # 10,000원으로 나눈몫.
change = change % 10000

cnt5000 = change // 5000    # 5,000원으로 나눈몫.
change = change % 5000

cnt1000 = change // 1000    # 1,000원으로 나눈몫.
change = change % 1000

print(f'50000원 : {cnt50000}')
print(f'10000원 : {cnt10000}')
print(f'5000원 : {cnt5000}')
print(f'1000원 : {cnt1000}')
print(f'530원 : {change}')
