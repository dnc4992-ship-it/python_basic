# ch09_lab5.py

w_see = []             # 보고싶은 동물
see = []                 # 본 동물
animal = []             # 동물원에서 본 동물입력
new_see = []      #  새롭게 본  동물입력


a = input(f' 보고 싶은 동물을 입력하세요 : ')       # 보고싶은 동물입력

b = input(f' 본 동물을 입력하세요 : ')                 # 본 동물입력


            if a == '없음':
            break
            w_see.append(a)

            
            if b == '없음':
            break          
            see.append(b)
            
#----------------------------------
            
           if see in w_see:
             w_see.remove(see)

           else :
                new_see.append(w_see)
                               )

print(f'아직 보지 못한 동물은 :{w_see}')
print(f'새롭게 본 동물은 :{new_see}')
