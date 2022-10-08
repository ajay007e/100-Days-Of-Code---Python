from turtle import Turtle
from random import randint,choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE
        self.create()
    
    def create(self):
        c = Turtle("square")
        c.shapesize(1,2)
        c.penup()
        c.color(choice(COLORS))
        c.setheading(180)
        c.goto(300,randint(-250,250))
        self.cars.append(c)

    
    def move(self):
        for c in self.cars:
            c.forward(self.distance)
    
    def nextLevel(self):
        self.distance += MOVE_INCREMENT
