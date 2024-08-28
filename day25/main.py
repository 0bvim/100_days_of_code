### doing with csv
# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatatures.append(row[1])
			
# 	print(temperatatures)

### doing with pandas

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) # dataframe
# print(data["temp"]) # series (single column)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create a brand new data frame

data_ditc = {
        "students": ["Stete", "Lila", "Nivi"],
        "scores": [100, 101, 100]
}

new_frame = pandas.DataFrame(data_ditc)
print(new_frame)

# convert to CSV file

new_frame.to_csv("new_frame.csv")
