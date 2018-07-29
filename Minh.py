from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 0
n = 3
for i in range(5):
    for o in range(n):
        m = colors[c]
        pencolor(m)
        forward(100)
        left(360/n)
    n +=1
    c +=1
mainloop()

