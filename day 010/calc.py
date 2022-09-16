
def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}


def calc():
  from art import logo
  print(logo)
  num1 = float(input("Enter first number:"))
  choice = "y"
  while choice == "y":
    for symbol in operations:
      print(symbol)
    symbol = input("pick an operation:")
    num2 = float(input("Enter next number:"))

    function = operations[symbol]
    result = function(num1,num2)
    print(f"{num1} {symbol} {num2} = {result}")
    choice = input(f'Type "y" to continue with {result} , or type "n" to new calculation:').lower()
    if choice == "y":
      num1 = result
    elif choice == "n":
      calc()
    #   import replit
    #   replit.clear()

calc()