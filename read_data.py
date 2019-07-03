import csv
import re

with open('merged.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    durchmesser = False
    vorzeichen = "nix"
    text = True
    isos = []
    dimensions = []
    for row in csv_reader:
        line_count += 1

        if "ISO" in row[1]:
            isos.append(row[1])
        if durchmesser:
            #print("Durchmesser: " + row[1])
            dimensions.append("Durchmesser: " + row[1])
            durchmesser = False
            continue
        if row[1] == "%%c":
            durchmesser = True
        if row[1] == "-" or row[1] == "+":
            vorzeichen = row[1]
        isnumber = re.findall(r"\d*\,\d+", row[1])
        if isnumber:
            if vorzeichen != "nix":
                #print(vorzeichen + isnumber[0])
                dimensions.append(vorzeichen + isnumber[0])
            else:
                if row[1][0]!="?":
                    #print(isnumber[0])
                    dimensions.append(isnumber[0])
            vorzeichen = "nix"
        if row[1][0] == "?":
            #print("+/- " + row[1][1:])
            dimensions.append("+/- " + row[1][1:])

    print(isos)
    #print(dimensions)
    print(f'Processed {line_count} lines.')

    dim = []
    dim_count = 0
    for x in dimensions:
        if x == "Durchmesser: ":
            dim_count = 0
        if dim_count > 2:
            dim_count = 0
        if dim_count == 0:
            print("Maße: " + "\n" + x)
            dim_count += 1
            continue
        if dim_count == 1:
            print ("Toleranzen: " + "\n" + x)
            dim_count += 1
            if "+/-" in x:
                dim_count += 1
            continue
        if dim_count == 2:
            print(x)
            dim_count += 1
            continue


