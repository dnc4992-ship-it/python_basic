# ch08_lab7.py

import turtle as t

def draw_rect(x,y,d):
    # x,y좌표로 이동
    t.up()
    t.goto(x,y)
    t.down()

    # size 사각형 그리기
    for x in range(4):
        t.forward(d)
        t.left(90)
        
draw_rect(200, 200, 100)  # (200, 200)좌표에 한 변의 길이가 100px인 사각형 그리기
draw_rect(-200, -200, 50)
