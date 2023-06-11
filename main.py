# with open("data.csv") as data:
#   data =data.readlines()
#   print(data)


# import csv

# with open("data.csv") as data:
#   data =csv.reader(data)
#   temperature = []
#   for row in data:
#     if row[1] != "temp":
#       temperature.append(int(row[1]))
      
#   print(temperature)

import pandas
data =pandas.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# average and max temp
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day== "Monday"])
# print(data[data.temp==data.temp.max()])


# Create dataframe from scratch
data_dict ={
  "student":["Amy","james","Angela"],
  "scores":[76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_file.csv")

