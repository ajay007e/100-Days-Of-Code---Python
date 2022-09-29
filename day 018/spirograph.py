from turtle import Turtle,Screen
from random import choice,randint

t = Turtle()
t.shape('turtle')
# t.pensize(1)
t.speed(0)

s = Screen()
s.colormode(255)


i=0
while i<72:
    color = (randint(1,255),randint(1,255),randint(1,255),)
    t.pencolor(color)
    t.circle(100)
    t.right(5)
    i+=1



s.exitonclick()