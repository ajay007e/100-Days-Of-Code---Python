import pandas as pd

# import csv
# with open("day 025/weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temp.append(row[1])
#     print(temp)                                       // task 1 : csv reading using csv package



data = pd.read_csv("day 025/weather_data.csv")
print(data)
print(data["temp"])                                   


