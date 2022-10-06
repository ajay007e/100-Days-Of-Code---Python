from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        # self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        # self.goto(x,y)
        self.color("white")

    
    def move(self):
        sleep(0.1)
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    

    def bounce(self):
        self.y_move *= -1

