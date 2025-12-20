# ch09_lab7.py

want = []

while True :
    user = input('가고싶은 여행지는?')
    if user == '없음':
        break

    want.append(user)

cnt = len(want)

print(f'최종 희망 여행 리스트 :{want}')
print(f'총 희망 여행지 : {cnt}개')
