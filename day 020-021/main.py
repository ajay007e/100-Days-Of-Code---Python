from turtle import Screen
from snake import Snake
from food import Food
from score import Score


s = Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_on =True

while game_on:
    s.update()
    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        snake.add()
        score.add_score()
    
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        score.reset()
        snake.reset()


    for seg in snake.segment[1:] :
        if snake.head.distance(seg) <= 10: 
            score.reset()
            snake.reset()




s.exitonclick()