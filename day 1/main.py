def printing():
    print("Day 1 - Python Print Function")
    print("The function is declared like this:")
    print("print('what to print')")

def debugging():
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")

def input_function():
    name =  input("What is your name?")
    print(len(name))

def variable_swap():
    # 🚨 Don't change the code below 👇
    a = input("a: ")
    b = input("b: ")
    # 🚨 Don't change the code above 👆

    ####################################
    #Write your code below this line 👇

    a,b = b,a


    #Write your code above this line 👆
    ####################################

    # 🚨 Don't change the code below 👇
    print("a: " + a)
    print("b: " + b)

def band_name_generator():
    #1. Create a greeting for your program.
    print("Welcome to Band Name Generator..")
    #2. Ask the user for the city that they grew up in.
    cityName = input("What is the name of your city ?\n")
    #3. Ask the user for the name of a pet.
    petName = input("What is the name of the pet ?\n")
    #4. Combine the name of their city and pet and show them their band name.
    print("Your Band name is "+cityName+" "+petName)
    #5. Make sure the input cursor shows on a new line, see the example at:
    #   https://band-name-generator-end.appbrewery.repl.run/



