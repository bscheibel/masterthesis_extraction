import csv
import re


def read_dimensions(file_out, num):
    with open(file_out) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        durchmesser = False
        vorzeichen1 = "nix"
        is2vorzeichen = False
        vorzeichen2 = "nix"
        isos = []
        dimensions = []

        for row in csv_reader:
            #print(row)
            line_count += 1

            if "ISO" in row[num]:
                isos.append(row[num])

            if durchmesser:
                #print("Durchmesser: " + row[1])
                dimensions.append("Durchmesser: " + row[num])
                durchmesser = False
                continue

            if row[num] == "%%c":
                durchmesser = True
                continue

            if vorzeichen1 != "nix" and (row[num] == "-" or row[num] == "+"):
                is2vorzeichen = True
                vorzeichen2 = row[num]
                continue

            if row[num] == "-" or row[num] == "+":
                vorzeichen1 = row[num]
                continue

            isnumber = re.findall(r"\d*\,\d+", row[num]) #regex to get number out of line

            if isnumber:
                print(isnumber)
                if vorzeichen1 != "nix":
                    #print(vorzeichen + isnumber[0])
                    dimensions.append(vorzeichen1 + isnumber[0])
                else:
                    if row[num][0]!="?":
                        #print(isnumber[0])
                        dimensions.append(isnumber[0])
                if is2vorzeichen is True:
                    vorzeichen1 = vorzeichen2
                    is2vorzeichen = False

            if row[num][0] == "?":
                #print("+/- " + row[1][1:])
                dimensions.append("+/- " + row[num][1:])

        #print(isos)
        print(dimensions)
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
                print("Toleranzen: " + "\n" + x)
                dim_count += 1
                if "+/-" in x:
                    dim_count += 1
                continue
            if dim_count == 2:
                print(x)
                dim_count += 1
                continue


