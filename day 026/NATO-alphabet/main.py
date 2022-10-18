# import pandas as pd
# #TODO 1. Create a dictionary in this format:
# data = pd.read_csv("day 026/NATO-alphabet/nato_phonetic_alphabet.csv")
# nato_alphabets = {word["letter"]:word["code"] for (index,word) in data.iterrows()}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Please enter the word you want to code:")
# code_list = [nato_alphabets[letter.upper()] for letter in user_input]
# print(code_list)

#TODO updatting the code in such a way that only valid letters are accepting

import pandas as pd
data = pd.read_csv("day 026/NATO-alphabet/nato_phonetic_alphabet.csv")
nato_alphabets = {word["letter"]:word["code"] for (index,word) in data.iterrows()}
# code_list = None
while True:
    user_input = input("Please enter the word you want to code:")
    try:
        code_list = [nato_alphabets[letter.upper()] for letter in user_input]
        break
    except KeyError:
        print("Sorry, Only letters in the alphabets are allowed")
print(code_list)