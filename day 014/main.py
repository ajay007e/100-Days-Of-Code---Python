import art
import random
from game_data import data
#from replit import clear

def campare(first,second):
    if data[first]["follower_count"] > data[second]["follower_count"] :
        return "A"
    elif data[first]["follower_count"] < data[second]["follower_count"] :
        return "B"
    else :
        return "Draw"

gameover = False
score = 0

first_title = random.randint(0,49)

while not gameover:
    #logo
    print(art.logo)
    second_title = random.randint(0,49)
    while first_title == second_title:
        second_title =  random.randint(0,49)

    print(f'Comapare A :{data[first_title]["name"]},{data[first_title]["description"]},{data[first_title]["country"]}')

    print(art.vs)

    print(f'Against B :{data[second_title]["name"]},{data[second_title]["description"]},{data[second_title]["country"]}')

    choice = input("Who has more followewrs , type 'A' or 'B' :").upper()
    result = campare(first_title,second_title)
    if choice == result:
        score += 1
        #clear()
        print(f"You're right , Your Score : {score}")
        if choice == "B":
            first_title = second_title
    else:
        gameover = True
        #clear()
        print(art.logo)
        print(f"Sorry , That's wrong . Final score : {score}")

