# 음료수 캔 구매량 계산.py

student = int(input('음료수 마실 학생은?'))

drink = 2           # 1명당 = 2개씩
              
pack =  6           # 1pack = 6개



# 필요한 전체 음료수 개수

total_drink = student * drink     #  학생당 필요한 음료수량
 

# 필요한 팩 수 계산 (몫)


packs = total_drink // pack



if  total_drink % pack > 0 :             #  학생이 

    packs += 1
    


print(f'총 {packs}팩을 사야 합니다.')
