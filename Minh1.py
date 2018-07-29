from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 0
for i in range(5):
    for o in range(2):
        pencolor(colors[c])
        fillcolor(colors[c])
        begin_fill()
        forward(50)
        left(90)
        forward(100)
        left(90)
        end_fill()
    forward(50)
    c +=1
mainloop()
