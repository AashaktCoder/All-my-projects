import csv

with open("dataFile.csv", "r") as f:
    r = csv.reader(f)
    for i in r:
        print(i)
