# ch05_lab7.py

h = float(input('키(cm) : '))
print()

w = float(input('몸무게(kg) : '))
print()


# 입력받은 키(cm) -> (m) 환산

c_h = h / 100


# bmi = 몸무게/(키의 제곱)

bmi = float(w / (c_h)**2)


if bmi <=  20 :

    print(f'당신의 체질량 지수는 {bmi:.2f}(저체중)입니다.')



elif 20 <= bmi<= 25 :

    print(f'당신의 체질량 지수는 {bmi:.2f}(정상)입니다.')



elif  25 <= bmi <=  30 :

    print(f'당신의 체질량 지수는 {bmi:.2f}(과체중)입니다.')

   
else :  

    print(f'당신의 체질량 지수는 {bmi:.2f}(비만)입니다.')



