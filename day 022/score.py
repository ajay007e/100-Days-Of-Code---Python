from turtle import Turtle

ALIGN="center"
FONT=("Courier",50,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.goto(0,200)
        self.write(arg=f"{self.l_score} : {self.r_score}",align=ALIGN,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over",align=ALIGN,font=FONT)

    def add_l_score(self):    
        self.l_score += 1
        self.clear()
        self.refresh()
    
    def add_r_score(self):    
        self.r_score += 1
        self.clear()
        self.refresh()

