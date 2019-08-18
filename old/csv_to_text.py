import pandas
import csv
import re
#data_df = pandas.read_csv("values_LH.csv", sep=",")
#print(data_df.head(3))

#data = data_df[["X1","Y1","X2","Y2"]]
#print(data)


def read_csv(file):
    text = []
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        for row in reader:
            text.append(row[2])
    csvFile.close()
    ###extract ISOs
    matches = []
    regex = r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?)"
    for line in text:
        match = re.findall(regex, line)
        if match:
            matches.append(match)

    print(matches)


    return text