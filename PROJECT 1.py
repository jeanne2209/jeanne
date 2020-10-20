import csv
with open("", "r") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)