# ch04_lab5.py      # 체질량지수(BMI)구하기


print("체질량지수(BMI) 구하기")

print()


height = input('키:  ')                          # 키 1.70m
height = int(height)

weight = input('몸무게 :  ')                     # 몸무게 75
weight = float(weight)
print()




bmi = int(weight) / float((height/100)** 2)       # 체질량지수= 몸무게(kg) / 키(m)/100(제곱)


print(f'당신의 체질량지수는{bmi}입니다.')
