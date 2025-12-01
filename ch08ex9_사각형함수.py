# ch08ex9_사각형함수

import turtle as t

def draw_poly(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n)

t.up()
t.goto(50,50)
t.down()

for i in range(3, 9):
    draw_poly(i)
