from turtle import Screen
from paddle import Paddle


s = Screen()
s.setup(800,600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)

r_p = Paddle(350,0)
l_p = Paddle(-350,0)

s.listen()
s.onkey(r_p.up,"Up")
s.onkey(r_p.down,"Down")
s.onkey(l_p.up,"w")
s.onkey(l_p.down,"s")

game_on =True
while game_on:
    s.update()


s.exitonclick()