import csv
import ast
import re

with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfromHTML_layout_LH.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        reg = r",\s*'(\w*\W*.\d*)']"
        reg_search = re.findall(reg, row[2])
        print(reg_search)
