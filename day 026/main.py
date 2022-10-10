def SquaringNumbers():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    # 🚨 Do Not Change the code above 👆

    #Write your 1 line code 👇 below:

    squared_numbers = [ n*n for n in numbers]

    #Write your code 👆 above:

    print(squared_numbers)


def filterEvenNumbers():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    # 🚨 Do Not Change the code above

    #Write your 1 line code 👇 below:

    result = [n for n in numbers if n%2==0]

    #Write your code 👆 above:

    print(result)


def dicComprehension():
    with open("file1.txt") as file1:
        data1 = file1.readlines()

    with open("file2.txt") as file2:
        data2 = file2.readlines()
    
    result = [int(number) for number in data1 if number in data2]


    # Write your code above 👆

    print(result)