import random

def heads_tails():
    # 🚨 Don't change the code below 👇
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    # 🚨 Don't change the code above 👆 It's only for testing your code.
        
    #Write the rest of your code below this line 👇
    n = random.randint(0,1)
    if n == 1 : print('Heads')
    else: print("Tails")

def banker():
    # 🚨 Don't change the code below 👇
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)

    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    n = random.randint(0,(len(names)-1))
    print(n)
    print(f"{names[n]} is going to buy the meal today!")

def tressureMap():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = int(input("Where do you want to put the treasure? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    row = position %10
    position //=10
    map[row-1][position-1] = "X"

    #Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")    

def rockPaperScissors():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    print("Welcome to Rock Paper Scissors Game")
    choice1 = int(input("0 for Rock, 1 for Paper, 2 for Scissor:"))
    if(choice1 == 0):
        print(rock)
    elif(choice1 == 1):
        print(paper)
    elif(choice1 == 2):
        print(scissors)

    print("\nComputer choose:\n")

    choice2 = random.randint(0,2)
    if(choice2 == 0):
        print(rock)
    elif(choice2 == 1):
        print(paper)
    elif(choice2 == 2):
        print(scissors)

    if(choice1 == choice2):
        print("Draw")
    elif(choice1 == 0):
        if(choice2 == 1):
            print("You Lose")
        elif(choice2 == 2):
            print("You Win")
    elif(choice1 == 1):
        if(choice2 == 2):
            print("You Lose")
        elif(choice2 == 0):
            print("You Win")
    elif(choice1 == 2):
        if(choice2 == 0):
            print("You Lose")
        elif(choice2 == 1):
            print("You Win")
    else:
        print("You are not shown anything, You Lose")

