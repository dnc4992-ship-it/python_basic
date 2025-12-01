# ch08ex12_초기화.py

def init():
    global state

    if not state:
        state = True
        print('초기화를 진행합니다.')

    else:
        print("작동 중입니다.")

state = False
init()
init()
init()
