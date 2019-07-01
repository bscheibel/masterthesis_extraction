#if(+ oder - merge with next line)

#merge all values into one until 4 values or until no integer/string with number

import csv
import re

with open('merged.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    durchmesser = False
    text = True
    for row in csv_reader:
        if durchmesser:
            print("Durchmesser: " + row[1])
        durchmesser = False
        if row[1] == "%%c":
            durchmesser = True
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        isnumber = re.match(num_format, row[1])
        if isnumber:
            print(row[1])
        try:
            if row[1].isFloat():
                print(row[1])
        except:
            pass
        if row[1][0] == "?":
            print("+/- " + row[1][1:])
        line_count += 1
    print(f'Processed {line_count} lines.')
