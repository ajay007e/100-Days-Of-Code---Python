# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
dic = {}
def add(name,bid):
  dic[name] = bid

def winner():
  flag = ""
  top = 0
  for key in dic:
    if int(dic[key]) > int(top):
      top = int(dic[key])
      flag = key
  print(logo)
  print(f"{flag} win the bid with a price of ${top}")

print(logo)
print("Welcome to Bid")

is_end = False
while not is_end:
  name = input("Enter your Name:")
  bid = input("Enter your bid: $ ")
  add(name=name,bid=bid)
  more = input('More people for bid ? "y" to coninue, "n" to stop and wait for result:').lower()
  if more == "n":
#     clear()

#   elif more == "n":
    is_end = True
    # clear()

winner()