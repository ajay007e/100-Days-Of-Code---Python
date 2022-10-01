from turtle import Turtle,Screen

t = Turtle()
s = Screen()
s.listen()

def forward():
    t.forward(5)

def backward():
    t.backward(5)

def clock():
    t.right(5)

def anticlock():
    t.right(-5)

def clear():
    t.home()
    t.clear()


s.onkey(forward,"w")
s.onkey(backward,"s")
s.onkey(clock,"d")
s.onkey(anticlock,"a")
s.onkey(clear,"c")





s.exitonclick()
