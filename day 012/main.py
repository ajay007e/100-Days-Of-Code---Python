
import random
from art import logo

print(logo)

print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 100")
number = random.randint(1,100)

difficulty = input("Choose a difficulty ; Type 'easy' or 'hard':").lower()
if difficulty == "easy":
    chances = 10
elif difficulty == "hard":
    chances = 5

gameover = False

while not gameover:
    print(f"You have {chances} attempts remaining to guess the number")
    guess = int(input("Make a Guess:"))
    if guess == number:
        print(f"You got it, the number is {number}")
        gameover = True
    else:
        chances -= 1
        if guess > number:
            print("Too High")
        else:
            print("Too low")
        if chances == 0:
            gameover = True
            print(f"You run out of chances, You Lose. The number is {number}")
        else:
            print("Try again")
        