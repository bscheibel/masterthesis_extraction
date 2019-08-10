import csv


with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfromHTML_layout_LH.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row[2])
