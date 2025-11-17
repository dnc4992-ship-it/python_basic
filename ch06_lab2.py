# ch06_lab2.py

n = 1       # 횟수
s= 0


while n <= 2:
    if n % 2 == 1:  # 홀수일때
       s = s + n

    else :
        s = s-n

    n = n+1
print(s)

