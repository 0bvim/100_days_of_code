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
print(type(data)) # dataframe
print(data["temp"]) # series (single column)
