import csv
import math

def printsection(buffer, file_out):
    #print(b)
    obj = dict(zip(buffer[::2], buffer[1::2]))
    for keys, values in obj.items():
        if keys == '1':
            try:
                #print(values)
                #print('{},{}'.format(obj['10'], obj['20']))
                #print("\n")

                row = [values, math.floor(float(obj['10'])),math.floor(float(obj['20']))]
                with open(file_out, 'a') as csvFile:
                    writer = csv.writer(csvFile, delimiter =';')
                    if row[0] != '':
                        writer.writerow(row)

                csvFile.close()



            except:
                print("ERROR")
                #print(b)

    #if obj.get('1'):
    #    print('{}'.format(obj['1']))

def read(file, file_out):
    buffer = []
    file = open(file, "r")
    for line in file:
        line = line.strip()
        #print(line)
        if line == '100':         # we've started a new section, so
            printsection(buffer, file_out)      # handle the captured section
            buffer = []             # and start a new one
        buffer.append(line)
    printsection(buffer, file_out)
