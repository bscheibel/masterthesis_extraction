import csv
import math

def printsection(b):
    #print(b)
    obj = dict(zip(b[::2], b[1::2]))
    for keys, values in obj.items():
        if keys == '1':
            try:
                #print(values)
                #print('{},{}'.format(obj['10'], obj['20']))
                #print("\n")

                row = [values,math.floor(float(obj['10'])),math.floor(float(obj['20']))]
                with open('text.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile, delimiter =';')
                    if row[0] != '':
                        writer.writerow(row)

                csvFile.close()



            except:
                print("ERROR")
                #print(b)

    #if obj.get('1'):
    #    print('{}'.format(obj['1']))


buffer = []
file = open("Stahl_Adapterplatte.DXF", "r")
for line in file:
    line = line.strip()
    #print(line)
    if line == '100':         # we've started a new section, so
        printsection(buffer)      # handle the captured section
        buffer = []             # and start a new one
    buffer.append(line)
printsection(buffer)