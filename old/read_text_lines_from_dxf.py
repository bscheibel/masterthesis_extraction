import csv
import math

def printsection(buffer, file_out):
    obj = dict(zip(buffer[::2], buffer[1::2]))
    for keys, values in obj.items():
        if keys == '1':
            try:
                row = [values, math.floor(float(obj['10'])),math.floor(float(obj['20']))]
                with open(file_out, 'a') as csvFile:
                    writer = csv.writer(csvFile, delimiter =';')
                    if row[0] != '':
                        writer.writerow(row)

                csvFile.close()
            except:
                print("ERROR")


def read(file, file_out):
    buffer = []
    file = open(file, "r")
    for line in file:
        line = line.strip()
        #print(line)
        if line == '100':
            printsection(buffer, file_out)
            buffer = []
        buffer.append(line)
    printsection(buffer, file_out)


read("../drawings/sample.DXF", "sample.csv")