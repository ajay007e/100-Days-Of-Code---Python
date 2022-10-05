from turtle import Turtle
from time import sleep

class Snake:
    def __init__(self):
        self.starting_position = [(0,0),(-20,0),(-40,0)]
        # self.starting_position = [(0,0),(-5,0),(-10,0)]
        self.distance = 20
        self.segment =[]
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in range(3):
            t = Turtle("square")
            # t.shapesize(stretch_wid=0.5,stretch_len=0.5)
            t.penup()
            t.goto(self.starting_position[i])
            t.color("white")
            self.segment.append(t)

    def add(self):
        t = Turtle("square")
        # t.shapesize(stretch_wid=0.5,stretch_len=0.5)
        t.penup()
        t.goto(self.segment[-1].position())
        t.color("white")
        self.segment.append(t)
    
    def move(self,):
        sleep(0.1)
        for i in range(len(self.segment)-1,0,-1):
            x = self.segment[i-1].xcor()
            y = self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.head.forward(self.distance)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)