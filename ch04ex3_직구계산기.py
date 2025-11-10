# ch04ex3_직구계산기.py

ex_rate = 1430
pd = input('직구할 제품은? ')
price = input(f'{pd}제품의 가격($)은?')
price = float(price)
kr = price * ex_rate
print(f'{pd}제품의 가격은 {kr}원입니다.')
            

