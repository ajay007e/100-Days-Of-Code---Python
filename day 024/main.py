##TODO: Run this program to generate letter for the individuals

with open("day 024/Input/Names/invited_names.txt", "r") as f:
    content = f.read().split("\n")
with open("day 024/Input/Letters/starting_letter.txt") as l:
    letter = l.read()
for name in content:
    out = letter.replace("[name]", name)
    with open(f"day 024/Output/ReadyToSend/letter_for_{name}.txt","w") as output:
        output.write(out)
   
