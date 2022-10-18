
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


#TODO 3 - exercise 1

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(3)

#TODO 4 - exercise 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        post["Likes"]
    except:
        pass
    else:
        total_likes = total_likes + post['Likes']

print(total_likes)
