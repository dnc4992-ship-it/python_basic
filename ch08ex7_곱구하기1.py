# ch08ex7_곱구하기2.py


def sumn(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


def factorial(s, e):
    f = 1
    for i in range(s, e + 1):
        f = f * i
    return s

print(sumn(10))
s = sumn(100)
print(s)

print(factorial(3, 5))
print(factorial(1,3))
