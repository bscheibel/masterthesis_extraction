import csv
import re

with open('merged.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    durchmesser = False
    vorzeichen = "nix"
    text = True
    for row in csv_reader:
        #row[1] = row[1].replace(",",".")
        if durchmesser:
            print("Durchmesser: " + row[1])
        durchmesser = False
        #continue
        if row[1] == "%%c":
            durchmesser = True
        if row[1] == "-" or row[1] == "+":
            vorzeichen = row[1]
            #print(vorzeichen)
        isnumber = re.findall(r"\d*\,\d+", row[1])
        if isnumber:
            if vorzeichen != "nix":
                print(vorzeichen + isnumber[0])
            else:
                print(isnumber[0])
            vorzeichen = "nix"

        if row[1][0] == "?":
            print("+/- " + row[1][1:])

        line_count += 1
    print(f'Processed {line_count} lines.')

