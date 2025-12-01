# ch08ex9_사각형함수-1.py

import turtle as t

def draw_poly(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n)

draw_poly(8)

# 3~9 각형 그리기

        
for i in range (3, 9):
   draw_poly(i)
