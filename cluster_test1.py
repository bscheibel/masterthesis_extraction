#go through csv file, speichern x und y
#dann loop durch alle anderen x und y:
#    if abstand x weniger als
#    if abstand y weniger als
#    dann selber cluster
#    alles in ein file/variable speichern und werte löschen??? oder markieren als bereits geclustert
#    alles durchgehen
#wenn alles durch dann neues x und y und nochmal alles von vorn


import csv
#csvfile = open('values.csv','r')
#spamreader1 = list(csv.reader(csvfile, dialect='excel', delimiter=','))
#csvFileArray = []
csvfile1 = open('values.csv', 'r')
spamreader1 = list(csv.reader(csvfile1, dialect='excel', delimiter=','))
csvfile1.close()
#print(spamreader1)
#csvfile = open('values.csv', 'r+')
new_rows_list = []
with open("values.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #print(row)
        x = row[5]
        #print(x)
        y = row[6]
        #print(y)
        for row1 in spamreader1:
            #print(row1)
            x1 = row1[5]
            #print(x1)
            y1 = row1[6]
            #print(abs(float(x1) - float(x)))
            #print(abs(float(y1) - float(y)))
            if (abs(float(x1) - float(x)) < 21.0) and (abs(float(y1) - float(y)) < 40.0): # and row[7] == False:
                #print(row)
                row[4] = row[4] + " " + row1[4]
                print(row[4])
                row[7] = True
                writer = csv.writer(csvfile)
                writer.writerow(row)
            new_row = [row[0], row[1], row[2],row[3],row[4],row[5],row[6]] #write all values, including new merged text
            new_rows_list.append(new_row)
csvfile.close()


file2 = open("merged_values.csv", 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()