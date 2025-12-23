# ch10_lab2.py

burger ={"치즈버거" : [5000, 558],
         "치킨버거" : [5500, 650],
         "불고기버거" : [6000, 670]
         }


a = burger['치즈버거'] 
print(f'치킨 버거 가격 :{a[0], a[1]}')

burger["불고기버거"] = 5900
print(burger)
#=======
print()
for k in burger.items():
    print(f'{k[0]}')
