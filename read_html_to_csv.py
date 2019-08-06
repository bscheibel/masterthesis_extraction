import re
import csv


with open("drawings/5129275_Rev01-GV12.html", "r") as f:
    with open('values_fromhtml_GV12.csv', 'w') as writeFile:
        for line in f.readlines():
            #print(line)
            row = []
            if "<word" in line:
                exMin = r"xMin=\"(\d*\.?\d*)"
                exMin = re.findall(exMin,line)[0]
                row.append(exMin)
                eyMin = r"yMin=\"(\d*\.?\d*)"
                eyMin = re.findall(eyMin,line)[0]
                row.append(eyMin)
                exMax = r"xMax=\"(\d*\.?\d*)"
                exMax = re.findall(exMax,line)[0]
                row.append(exMax)
                eyMax = r"yMax=\"(\d*\.?\d*)"
                eyMax = re.findall(eyMax,line)[0]
                row.append(eyMax)
                Text = r">(.+)<" #wieso wird was mit "" extrahiert???
                Text = re.findall(Text,line)[0]
                row.append(Text.replace(',','.'))
                avgX=(float(exMin)+float(exMax))/2.0
                row.append(avgX)
                avgY=(float(eyMin)+float(eyMax))/2.0
                row.append(avgY)
                row.append(False)
                writer = csv.writer(writeFile)
                writer.writerow(row)
    writeFile.close()

