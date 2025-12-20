# ch09_lab5a.py

want = []
new =[]

while True :
    user = input('보고 싶은 동물?')
    if user == '끝':
        break

    want.append(user)

print()
while True :
    seen = input('본 동물?')
    if seen == '끝':
        break

    if seen in want:
        want.remove(seen)
    else :
        new.append(seen)

print()
print(f'아직 못 본 동물 :{want}')
print(f'새롭게 본 동물 :{new}')
