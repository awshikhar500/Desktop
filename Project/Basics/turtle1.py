from turtle import * 

def square(d):
    for i in range(4):
        fd(d)
        lt(90)

def polygon(side=3, dis=50):
    for i in range(side):
        fd(dis)
        lt(360/side)


square(100)
polygon(5,100)
polygon(6,100)
polygon(7,100)
polygon(8,100)
hideturtle()
mainloop()