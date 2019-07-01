#if(+ oder - merge with next line)

#merge all values into one until 4 values or until no integer/string with number


#?0,05 equals +/- 0,5

import csv

with open('merged.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    durchmesser = False
    for row in csv_reader:
        if durchmesser:
            print("Durchmesser: " + row[1])
        durchmesser = False
        if row[1] == "%%c":
            durchmesser = True
        line_count += 1
    print(f'Processed {line_count} lines.')