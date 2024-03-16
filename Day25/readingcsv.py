# Reading CSV file
import csv #improting module to process csv data
#importing pandas module
import pandas
#opening file
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
#conversion to dictionary
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(round(average, 2))

#average using pandas
print(data["temp"].mean())
print(data["temp"].max())
data2 = data[data.temp == data.temp.max()]
print(data2)
#selecting column, be careful with letter-sensitive
print(data["condition"])

print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])

#checking monday temp and converting to F
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
mondaytempF = monday_temp * 9/5 + 32
print(mondaytempF)

#Creating dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data3 = pandas.DataFrame(data_dict)
print(data3)
data3.to_csv("new_data.csv")