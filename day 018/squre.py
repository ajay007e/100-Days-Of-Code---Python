from turtle import Turtle,Screen

t = Turtle()
t.shape('turtle')
t.color('red')

t.penup()
t.forward(50)
t.right(90)
t.forward(50)
t.pendown()
for _ in range(4):
    t.right(90)
    t.forward(100)


s = Screen()
s.exitonclick()