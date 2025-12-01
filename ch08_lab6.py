# ch08_lab6.py

import turtle as t

def drawpoly(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def draw():
        drawpoly(4)
        drawpoly(3)

for x in range(5):
    draw()
    t.forward(50)

