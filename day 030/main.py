
#TODO 1 - familarize with exception handling

try:
    file  = open("day 030/text.txt")
    dic = {"key":"value"}
    print(dic['kei'])
except FileNotFoundError:
    file  = open("day 030/text.txt","w")
    file.write("new file.")
except KeyError as e:
    print(f"The key  {e} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed successfully")
    # raise TypeError("This is the error that i made up.!")


#TODO 2 - user defined errors

height  = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3 : raise ValueError("Height must be less than or equal to 3")

print(f"BMI is {weight/(height**2)}")

