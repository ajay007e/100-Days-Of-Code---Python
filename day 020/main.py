from turtle import Turtle,Screen
from snake import Snake

s = Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_on =True

while game_on:
    s.update()
    snake.move()




s.exitonclick()