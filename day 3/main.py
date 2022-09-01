def even_or_odd():
    # 🚨 Don't change the code below 👇
    number = int(input("Which number do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    if (number % 2 == 0) : 
        print("This is an even number.")
    else: 
        print("This is an odd number.")

def bmi_2():
    # 🚨 Don't change the code below 👇
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    bmi = weight / ( height*height)

    print(f"Your BMI is {int(round(bmi))},",end=" ")
    if bmi < 18.5 : print("you are underweight.")
    elif bmi < 25 : print("you have a normal weight.")
    elif bmi < 30 : print("you are slightly overweight.")
    elif bmi < 35 : print("you are obese.")
    else : print("you are clinically obese.")

def leap_year():
    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    if (((year % 4 == 0 )and (year % 100 != 0)) or (year % 400 == 0 )):
        print("Leap year.")
    else: print("Not leap year.")

def pizza_order():
    # 🚨 Don't change the code below 👇
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ").lower()
    add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
    extra_cheese = input("Do you want extra cheese? Y or N ").lower()
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    total = 0
    if size == "s" : 
        total +=15
        if add_pepperoni == "y":
            total += 2
    elif size == "m" : 
        total +=20
        if add_pepperoni == "y":
            total += 3
    elif size == "l" : 
        total +=25
        if add_pepperoni == "y":
            total += 3
    if extra_cheese == "y" : total += 1

    print(f"Your final bill is: ${total}.")

def love_calculator():
    # 🚨 Don't change the code below 👇
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n").lower()
    name2 = input("What is their name? \n").lower()
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    t1 = 0
    for i in "true":
        for j in name1:
            if i == j : t1 +=1
        for j in name2 :
            if i == j : t1 +=1
    t2 = 0
    for i in "love":
        for j in name1:
            if i == j : t2 +=1
        for j in name2 :
            if i == j : t2 +=1
    total = t1*10+t2

    if ((total<10) or (90<total) ):
        print(f"Your score is {total}, you go together like coke and mentos.")
    elif ((total >40) and (total< 50)):
        print(f"Your score is {total}, you are alright together.")
    else:
        print(f"Your score is {total}.")

def treasure_island():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    if (input("You're at a cross road. Where do you want to go? Type 'left' or 'right'").lower()=='left'):
        if(input("You are at a lake.There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.")=='wait'):
            d=input("You arrive at the island unharmed.There is 3 doors. One red, one yellow and on blue.Which color do you choose?").lower()
            if d == "y": print("You Win!")
            else: print("Game Over!")
        else: print("Game Over")
    else: print("Game Over")

