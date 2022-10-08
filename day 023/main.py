import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
c = CarManager()
sc = Scoreboard()

screen.listen()
screen.onkey(p.move,"Up")

game_is_on = True
time_counter = 0
while game_is_on:
    if time_counter % 6 == 5:
        c.create()
    time.sleep(0.1)
    screen.update()
    c.move()
    time_counter += 1

    for car in c.cars:
        if car.distance(p) < 20:
            game_is_on = False
            sc.game_over()
    
    if p.ycor() >= FINISH_LINE_Y:
        c.nextLevel()
        p.restart()
        sc.addScore()

screen.exitonclick()
