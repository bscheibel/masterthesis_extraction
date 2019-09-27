import csv

def read(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=";")
        result = []
        dict = {}
        for row in reader:
            ausrichtung = row[1]
            row3 = row[2]
            row3 = eval(row3)
            element = ""
            ymin = 100000000.0
            ymax = 0.0
            xmin = 100000000.0
            xmax = 0.0
            coords = []

            merged_elements = []
            length = 0
            for e in row3:
                length += len(e)

            for elem in row3:

                #print("start")
                #print(len(elem))
                if len(row3) == 1:
                    element = elem[4]
                    xmin = float(elem[0])
                    ymin = float(elem[1])
                    xmax = float(elem[2])
                    ymax = float(elem[3])

                else:

                    if isinstance(elem[0],list):
                        merged_elements += elem

                        #print(length, len(merged_elements))
                        if len(merged_elements) < length:   ####woher weiß ich die länge????
                            #print("bb", len(merged_elements), len(elem))
                            continue

                        if int(ausrichtung) == 1:
                            #print(elem)
                            merged_elements = sorted(merged_elements, key=lambda k: [float(k[3])], reverse=True)

                        #print(merged_elements)

                        for elemt in merged_elements:
                            #print(merged_elements)
                            #print(elem)
                            element += elemt[4] + " "
                            if float(elemt[0]) < xmin:
                                xmin = float(elemt[0])
                            if float(elemt[1]) < ymin:
                                ymin = float(elemt[1])
                            if float(elemt[2]) > xmax:
                                xmax = float(elemt[2])
                            if float(elemt[3]) > ymax:
                                ymax = float(elemt[3])


                    else:
                        element += elem[4] + " "
                        if float(elem[0]) < xmin:
                            xmin = float(elem[0])
                        if float(elem[1]) < ymin:
                            ymin = float(elem[1])
                        if float(elem[2]) > xmax:
                            xmax = float(elem[2])
                        if float(elem[3]) > ymax:
                            ymax = float(elem[3])

            #print(element)
            result.append(element)
            coords.append(xmin)
            coords.append(ymin)
            coords.append(xmax)
            coords.append(ymax)
            dict[element] = coords
            #print("\n")

    return dict