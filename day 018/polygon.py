from turtle import Turtle,Screen
from random import choice

t = Turtle()
t.shape('turtle')
t.color('red')

colors = ['dim gray','dark blue','forest green','yellow green','gold','firebrick','hot pink','dark violet']


for j in range(4,11):
    angle = (360/j)
    print(angle)
    t.pencolor(choice(colors))
    for i in range(j):
        # t.pensize(11-j)
        t.right(angle)
        t.forward(100)


s = Screen()
s.exitonclick()