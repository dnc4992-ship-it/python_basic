# ch08ex6_합구하기.py

def total(n):
    t = 0
    for num in range(1, n+1):
        t += num
    return t

s1 = total(10)
print(s1)

s2 = total(100)
print(s2)
