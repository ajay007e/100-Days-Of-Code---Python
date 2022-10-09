from re import T
import turtle as tu
import pandas as pd

screen = tu.Screen()
screen.title("US States Game")
screen.addshape("day 025/us-states-game/blank_states_img.gif")
tu.shape("day 025/us-states-game/blank_states_img.gif") 

game_on = True
correct_answer = 0

data = pd.read_csv("day 025/us-states-game/50_states.csv")
states = data.state.to_list()

while game_on:
    
    ans = screen.textinput(f"{correct_answer}/50 Guess the State","Enter the name of the state you know ?").title()
    if ans :
        state = data[data.state == ans]
        if ans == "Close": game_on = False
        if not state.empty and ans in states:
            t = tu.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state.x),int(state.y))
            t.write(ans)
            correct_answer +=1
            states.remove(ans)
        if correct_answer == 50: game_on = False
    else: game_on = False
pd.DataFrame(states).to_csv("day 025/us-states-game/states_to_learn.csv")

    
