import csv

with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfrom_precomputed_dbscan.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        ausrichtung = row[1]
        row3 = row[2]
        row3 = eval(row3)
        element = ""
        merged_elements = []
        for elem in row3:

            if len(row3) == 1:
                print(elem[4])

            else:

                if isinstance(elem[0],list):
                    merged_elements += elem
                    #print(merged_elements)
                    if len(merged_elements) < len(row3):
                        continue
                    if int(ausrichtung) == 1:
                        elem = sorted(merged_elements, key=lambda k: [float(k[3])], reverse=True)

                    for elem in elem:
                        element += elem[4] + " "

                else:
                    element += elem[4] + " "


        print(element)

        print("\n")

