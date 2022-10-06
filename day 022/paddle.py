from turtle import Turtle
from time import sleep

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.distance = 20
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)
        self.color("white")

    
    def up(self):
        if self.ycor() <= 270:
            self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        if self.ycor() >= -270:
            self.goto(self.xcor(),self.ycor()-20)
