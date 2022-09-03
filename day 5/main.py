import random


def avgHeight():
    # 🚨 Don't change the code below 👇
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆


    #Write your code below this row 👇

    s = sum(student_heights)
    print(round(s/len(student_heights)))

def highestScore():
    # 🚨 Don't change the code below 👇
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    h = max(student_scores)
    print(f"The highest score in the class is: {h}")

def addEven():
    #Write your code below this row 👇
    t = 0
    for i in range(2,101,2):
        t +=i
    print(t)

def fizzBuzz():
    #Write your code below this row 👇

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 : print("FizzBuzz")
        elif i % 3 == 0 :print("Fizz")
        elif i % 5 == 0 : print("Buzz")
        else: print(i)

def passwordGenerator():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password_list = []

    for i in range(nr_letters):
        password_list.append(random.choice(letters))

    for i in range(nr_symbols):
        password_list += random.choice(symbols)

    for i in range(nr_numbers):
        password_list += random.choice(numbers)

    password =""
    random.shuffle(password_list)
    for i in password_list:
        password +=i
    print(password)



