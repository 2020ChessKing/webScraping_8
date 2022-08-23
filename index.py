import csv

data = []

#Get Data in List
with open("filtered_stars.csv") as file:
    file = csv.reader(file)

    for row in file:
        data.append(row)

#Get Data in Dictionary
data = data[1:]
final_data = []

for row in data:
    planet = {"Name": row[0], "Radius": row[1], "Mass": row[2], "Gravity": row[3], "Distance": row[4]}
    final_data.append(planet)

print(final_data)