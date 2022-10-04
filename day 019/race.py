from turtle import Turtle,Screen
from random import randint

s = Screen()
s.setup(width=500,height=400)
user_bet = s.textinput(title='make your bet',prompt="which turtle will win the race ?")
colors = ['red','green','blue','yellow','orange','purple']
ycor = [20,-20,60,-60,100,-100]
turtles = []

for i in range(6):
    t = Turtle(shape='turtle')
    t.penup()
    t.goto(x=-230,y=ycor[i])
    t.color(colors[i])
    turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() >= 200:
            is_race_on = False
            if t.pencolor() == user_bet.lower():
                print(f"you won the bet ! the {t.pencolor()} turtle win the race")
            else:
                print(f"you lose the bet ! the {t.pencolor()} turtle  win the race")

        t.forward(randint(1,10))










s.exitonclick()
