import csv
import re

with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfrom_precomputed_dbscan.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    reg_search = []
    for row in reader:
        reg = r",\s*'\(*(\w*\W*.,*\d*)\)*'\]*\]"
        #print(row[1])
        row3 = row[1]
        row3 = eval(row3)
        for blub in row3:
            #print(len(row3),row3)
            if len(row3) == 1:
                print(blub[4])
            else:

                if isinstance(blub[0],list):
                    for blubi in blub:
                        print(blubi[4])
                else:

                    print(blub[4])


        print("\n")
"""      reg_search.append(re.findall(reg, row[1]))
        #for reg in reg_search:
    for reg in reg_search:
            reg_new = reg
            #print(reg_new)
    ##print(data[labels == 0])"""

####TO DO: beim auslesen nach x-Koordinaten sortieren