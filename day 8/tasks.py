from math import ceil 

#Write your code below this line 👇
def paint_calc(height, width, cover):
    cans = ceil((height*width)/cover)
    print(f"You'll need {cans} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# ----------------------------------------------------------------------------------------------------

from math import sqrt

#Write your code below this line 👇
def prime_checker(number):
    for i in range(2,int(sqrt(n))):
        if n%i==0:
             print("It's not a prime number.")
             return
    print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# ----------------------------------------------------------------------------------------------------
