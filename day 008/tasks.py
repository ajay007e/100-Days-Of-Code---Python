from math import ceil 

#Write your code below this line ๐
def paint_calc(height, width, cover):
    cans = ceil((height*width)/cover)
    print(f"You'll need {cans} cans of paint")

#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# ----------------------------------------------------------------------------------------------------

from math import sqrt

#Write your code below this line ๐
def prime_checker(number):
    for i in range(2,int(sqrt(n))):
        if n%i==0:
             print("It's not a prime number.")
             return
    print("It's a prime number.")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)

# ----------------------------------------------------------------------------------------------------
