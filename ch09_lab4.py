# ch09_lab4.py

fruits = ['사과','바나나','딸기','키위','귤','수박','사과']
len(fruits)
fruits1 = len(fruits)
print(f'과일은 총{fruits1}개 입니다.')

fruits_cnt = fruits.count('사과')
print(f'사과의 개수 :{fruits_cnt}')

del fruits[-1]      # 마지막 과일을 삭제
print(fruits)

fruits.insert(2, '복숭아')    # 3번째에 복숭아 추가
print(fruits)

if '사과' in fruits:
    print('사과가 있다')
else:
    print('없다')
fruits_list = fruits[1:4] 
print(fruits_list)
print(f'2번째~4번째 과일은{fruits_list}')





