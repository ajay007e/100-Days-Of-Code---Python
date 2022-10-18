# TODO 1 - familarize with exception handling

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

