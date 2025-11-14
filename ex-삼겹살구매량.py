# 삼겹살 구매량 계산

home = int(input ('홈파티에 올사람은?'))

pig = 2              # 600g당 : 1근  -2명



pig1 = home // pig

if  home % 2 > 0 :

    pig1 += 1


print(f'홈파티에 필요한 돼지삼겹살은 {pig1}근 사야합니다.' )

