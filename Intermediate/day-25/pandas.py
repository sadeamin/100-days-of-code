# # with open("2.1 weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# # with open("2.1 weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas

# data = pandas.read_csv("2.1 weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(f"The average of temperature is : {average}")

# alternative:
# print(data["temp"].mean())

#
# print(data["temp"].max())

# alternative:
# print(max(data["temp"]))

#
# print(data["condition"])


# alternative:
# print(data.condition)

# get data in Row

# print(data[data.day == "Monday"])


# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = f"{monday_temp} Celsius in Fahrenheit: {monday.temp * 9 / 5 + 32}"
# print(monday_temp_F)

# Celsius to Fahrenheit formula : (C x 9/5) + 32 = F

# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)
#
# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")