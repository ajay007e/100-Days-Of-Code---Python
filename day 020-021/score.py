from turtle import Turtle

ALIGN="center"
FONT=("Arial",18,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hScore =0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score : {self.score} Highscore : {self.hScore}",align=ALIGN,font=FONT)

    def reset(self):
        if self.score > self.hScore:
            self.hScore = self.score
        self.score = 0
        self.refresh()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"Game Over",align=ALIGN,font=FONT)

    def add_score(self):    
        self.score += 1
        self.refresh()

