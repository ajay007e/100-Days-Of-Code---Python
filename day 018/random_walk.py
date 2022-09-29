from turtle import Turtle,Screen
from random import choice,randint

t = Turtle()
t.shape('turtle')
t.pensize(5)
t.speed(0)

s = Screen()
s.colormode(255)

angles=[-180,180,90,-90]

i=0
while i<1000:
    # t.pencolor(choice(colors))
    color = (randint(1,255),randint(1,255),randint(1,255),)
    t.pencolor(color)
    t.forward(30)
    t.right(choice(angles))
    i+=1



s.exitonclick()