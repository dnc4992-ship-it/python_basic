# ch08ex6_합구하기1.py

def sumn(n):
    s = 0
    for i in range(1, n+1):
        s += s + i
    return s

print(sumn(10))
s = sumn(100)
print(s)
