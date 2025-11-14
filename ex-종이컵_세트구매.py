# 종이컵_세트구매.py


party_man =int(input('모임 인원이 몇명입니까?'))

print()


# 모인인원에 /필요한 종이컵 필요수량

man = 2     # 1컵 = 2명

cap = 50    # 1set = 50 ea


# 입력된 인원의필요한 컵

need_cup = party_man * man

buy_cup = need_cup // 50


if need_cup % 50 > 0 :
    
    buy_cup += 1


print(f'필요한 컵은 {buy_cup}세트를 사야합니다.')
