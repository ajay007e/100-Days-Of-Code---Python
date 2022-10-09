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



# data = pd.read_csv("day 025/weather_data.csv")
# print(data)
# print(data["temp"])                                   // task 2 : csv reading using pandas package



# data = pd.read_csv("day 025/weather_data.csv")

# ## dataframe into dictionary
# data_dict = data.to_dict()
# print(data_dict)

# ## series into list
# data_list = data["temp"].to_list()
# print(data_list)

# ## row selection using the pandas package
# print(data.temp)

# ## methods in the pandas package
# print(data["temp"].mean())

# ## column selection using pandas package
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max() ])

# ## creating dataframe using pandas package
# data_dic = {
#     "students":["Ajay", "Amal", "Praveen"],
#     "scores":[20,30,40]
# }
# data = pd.DataFrame(data_dic)

# ### to create csv from dataframe
# data.to_csv("day 025/new_csv.csv")                    // pandas package familarization



# data = pd.read_csv("day 025/Squirrel_Data.csv")
# black = data[data["Primary Fur Color"] == "Black"].index
# gray = data[data["Primary Fur Color"] == "Gray"].index
# cinnamon = data[data["Primary Fur Color"] == "Cinnamon"].index

# dic = {
#     "fur_color": ["Black","Gray","Cinnamon"],
#     "count":[len(black),len(gray),len(cinnamon)]
# }
# pd.DataFrame(dic).to_csv("day 025/fur_data.csv")      //squirrel data analysis using the pandas package
