import csv

## open CSV file and rea it
myfile  = open('text.csv', "r")
reader = csv.reader(myfile, delimiter=";")
## create an empty dictionary
mydictionary = {}

rownum = 0

for row in reader:
    ## check if it is the header
    if rownum == 0:
        pass
    else:
        ## split the line of CSV in elements..Use the name for the key in dictionary and the other two in a list
        #line = row.split(";")
        #print(row)
        text = row[0]
        #print(text)
        x = row[1]
        y = row[2]

        if x in mydictionary:
            mydictionary[text][1] += text
            print(mydictionary[text][1] )
        else:
            mydictionary[text] = [x,y]

    rownum += 1

myfile.close()

## create a new list of lists with the data from the dictionary
newcsvfile = ["text","x","y"]

for i in mydictionary:
    newcsvfile.append(mydictionary[i])

## write the new list of lists in a new CSV file
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(newcsvfile)