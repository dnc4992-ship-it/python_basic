# ch10_lab1.py

calendar = {"1월": 31,"2월" : 28, "3월": 31, "4월" : 30}

for month, day in calendar.items():
    
    print(f'{month}은 {day}일 까지 있습니다.')
#===================
print()

# 1) 2월을 29일로 변경
calendar["2월"] =29
for month, day in calendar.items():
    print(f'{month}은 {day}일 까지 있습니다.')

#===================
# 2) 5월을 31일로 추가
print()
calendar["5월"] =31
for month, day in calendar.items():
      print(f'{month}은 {day}일 까지 있습니다.')
