# ch09_lab4.py

zoo =['곰','강아지','고양이','사자','호랑이',
    '여우','늑대','원숭이','뱀','코끼리']

like =[]
hate = []
answer = []

for a in zoo :
    answer = input( f'{a}를 좋아하세요?')
    if answer == 'y' :
       like.append(a)

    elif answer == 'n':
        hate.append(a)

print(f'좋아하는 동물:{like}')
print(f'좋아하지 않는 동물:{hate}')

        
    
