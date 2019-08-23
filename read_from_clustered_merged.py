import csv
import re

with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfrom_precomputed_dbscan.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    reg_search = []
    for row in reader:
        reg = r",\s*'\(*(\w*\W*.,*\d*)\)*'\]*\]"
        reg_search.append(re.findall(reg, row[2]))
        #for reg in reg_search:
    for reg in reg_search:
            reg_new = reg
            print(reg_new)
    ##print(data[labels == 0])
