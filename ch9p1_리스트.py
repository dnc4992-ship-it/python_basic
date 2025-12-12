# ch9p1_리스트.py

a = [ 1, 3, 5, 4, 9]

student  = ['홍길동', 18, '김철수', 40 , '김영수', 17]
print(student)

# 인덱싱

print(a[0]) # 리스트 [ 인덱스]
print(a[2])
print(student[2], student[3])

# 슬라이싱
print(a[1:4])
print(student[0:2])

# ['김철수', 40]
print(student[2:4])
print()
print(student[:2])
print()
print(student[2:])

print(a[-1])
print(a[-2])
print(student[-2:])

print(a[::2])   #[시작:종료+1:증감]

# 원소 변경
a[0] = 10
print(a)
print()

# 원소 제거
del a[1]
print(a)
print()

# 리스트 연산
print(a + student)
print()

new = a + student
print()
print(new)

              
