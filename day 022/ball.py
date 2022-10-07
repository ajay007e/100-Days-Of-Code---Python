from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.1
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        # self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        # self.goto(x,y)
        self.color("white")

    
    def move(self):
        sleep(self.ball_speed)
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *=0.9
    
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *=.9

    def reset(self):
        self.ball_speed  = 0.1
        self.goto(0,0)
        self.bounce_x()

