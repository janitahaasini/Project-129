import csv
data=[]
with open("dataset_2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]
#converting all the planets to lower case
for i in planet_data:
    i[2]=i[2].lower()
#sorting the planet name in alphabetic order
planet_data.sort(key=lambda planet_data:planet_data[2])
with open ("sorted_data.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)