import csv
import re


def read_dimensions(file_out, num):
    toleranzen_included = False
    
    with open(file_out) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            #print("test")
            if row[num] == "-" or row[num] == "+":
                toleranzen_included = True
            #    print("test2")

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
            #print(line_count)

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
            if (row[num] == "-" or row[num] == "+") and ismaybenumber:
                dimensions.append(ismaybenumber[0])

            if row[num] == "-" or row[num] == "+":
                vorzeichen1 = row[num]
                continue

            if "%%c<>" in row[num]:
                continue

            if "2x %%c" in row[num]:
                continue

            if "16%" in row[num]:
                continue
            if "R" in row[num][0] and not "Rz" in row[num]:
                dimensions.append("Radius: " + row[num][1:])
                continue

            isnumber = re.findall(r"\d*\,\d+|\d*\.\d+", row[num][0:6]) #regex to get number from line
            ismaybenumber = re.findall(r"^[0-9]+$",row[num])
            if isnumber:
                #print(isnumber)
                if vorzeichen1 != "nix":
                    if vorzeichen1 == "-" and (row[num] == "0,00" or row[num] == "0,0"):
                        dimensions.append(row[num])
                    else:
                    #print(vorzeichen + isnumber[0])
                        dimensions.append(vorzeichen1 + isnumber[0])
                        vorzeichen1 = "nix"
                else:
                    if row[num][0]!="?":
                        #print(isnumber[0])
                        dimensions.append(isnumber[0])
                if is2vorzeichen is True:
                    vorzeichen1 = vorzeichen2
                    is2vorzeichen = False
                    vorzeichen2 = "nix"


            if row[num][0] == "?" and row[num][1].isdigit():
                #print("+/- " + row[1][1:])
                dimensions.append("+/- " + row[num][1:])

        if isos.__len__()>0:
            print(isos)
        else:
            print("No regulations found.")
        #print(dimensions)
        print(f'Processed {line_count} lines.')

        dim = []
        dim_count = 0
        if not toleranzen_included:
            print("Maße")
        for x in dimensions:
            if not toleranzen_included:
                print(x)
                continue
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



