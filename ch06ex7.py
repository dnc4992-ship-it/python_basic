
# ch06ex7.py

import turtle as t


t.bgcolor('black')
t.speed(0)
t.setup(500, 500)

angle = 119


for d in range(500):
    if d % 3 == 0:
        color = 'red'
    elif d % 2 == 1:
        color = 'yellow'
   
    else:
        color = 'green'
        
    t.color(color)
    t.forward(d)
    t.left(angle)

t.mainloop()
