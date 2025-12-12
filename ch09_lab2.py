# ch09_lab2.py

bs = ['파이썬', 'C', '캐드', '포토샵', 'JAVA', '엑셀']
print(f'{bs}')

bs.append('파워포인트')
print(f'{bs}')
bs.remove('JAVA')
print(f'{bs}')
bs.insert(4,'일러스트')
print(f'{bs}')
cnt =len(bs)
print(f'도서 수는 {cnt}권입니다.')

item  = input('도서 이름 : ')

if item in bs:  
    print(f" '{item}'은 대여 가능합니다.")
else :
    print(f" '{item}은 대여 가능하지 않습니다.")
