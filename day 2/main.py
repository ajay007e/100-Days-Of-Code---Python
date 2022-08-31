def data_type():
    # 🚨 Don't change the code below 👇
    two_digit_number = input("Type a two digit number: ")
    # 🚨 Don't change the code above 👆

    ####################################
    #Write your code below this line 👇
    a = int(two_digit_number[0])
    b = int(two_digit_number[1])
    c = a+b

    print(c)

def bmi_calculator():
    # 🚨 Don't change the code below 👇
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    bmi = float(weight) / ( float(height)*float(height))
    print(int(bmi))

def life_in_weeks():
    # 🚨 Don't change the code below 👇
    age = input("What is your current age?")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    r = 90 - int(age)
    z = r *12
    y = r*52
    x = r*365

    print(f"You have {x} days, {y} weeks, and {z} months left.")


def tip_calculator():
    print("Welcome to the tip calculator.")
    total = float(input("What was the total bill ?"))
    percent = int(input("What percent of tip would you like to give ?"))
    people = int(input("How many people to split the bill ?"))
    tip = round(((total *(1+(percent/100)))/people),2)
    print(f"Each person should pay ${tip} ")

tip_calculator()
