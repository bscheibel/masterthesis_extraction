import csv

with open("/home/bscheibel/PycharmProjects/dxf_reader/values_clusteredfrom_precomputed_dbscan.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    reg_search = []
    for row in reader:
        ausrichtung = row[1]
        row3 = row[2]
        row3 = eval(row3)
        element = ""
        merged_elements = []
        for blub in row3:

            #print(row3)

            if len(row3) == 1:
                print(blub[4])
                #print("blub")
            else:

                if isinstance(blub[0],list):
                    merged_elements += blub
                    print(merged_elements)

                    if int(ausrichtung) == 1:
                        blub = sorted(merged_elements, key=lambda k: [float(k[3])],reverse=True)

                    for blubi in blub:
                        element += blubi[4] + " "

                else:
                    element += blub[4] + " "


        #print(element)


        print("\n")

