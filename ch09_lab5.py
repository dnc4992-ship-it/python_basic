# ch09_lab5.py

w_see = []             # 보고싶은 동물
see = []                 # 본 동물
new_see = []      #  새롭게 본  동물입력


while True:
    
            a = input(f' 보고 싶은 동물을 입력하세요 : ')       # 보고싶은 동물입력
            if a == '없음':
                break
            w_see.append(a)

            
         
            
#----------------------------------
 while True:
     
           b = input(f' 본 동물을 입력하세요 : ')                 # 본 동물입력
           if b == '없음':
                break
            
            see.append(b)
            
           if b in w_see:
             w_see.remove(see)

           else :
                new_see.append(w_see)
                           

print(f'아직 보지 못한 동물은 :{w_see}')
print(f'새롭게 본 동물은 :{new_see}')
