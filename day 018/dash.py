from turtle import Turtle,Screen

t = Turtle()
t.shape('turtle')
t.color('red')

t.right(-45)
t.penup()
t.backward(150)
t.pendown()

for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown() 



s = Screen()
s.exitonclick()