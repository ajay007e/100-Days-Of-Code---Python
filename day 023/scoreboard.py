from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.goto(-280,260)
        self.write(arg=f"score:{self.score} ",font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over",align="center",font=FONT)

    def addScore(self):    
        self.score += 1
        self.clear()
        self.refresh()
    
