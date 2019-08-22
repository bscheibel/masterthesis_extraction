import numpy as np
import pandas
import csv
from math import sqrt

def get_average_xy(list_input):
    csv_name = "temporary/list_to_csv_with_corner_points.csv"
    new_list = []
    resultFile = open(csv_name, 'w')
    wr = csv.writer(resultFile, delimiter=";")
    wr.writerow(["element", "xmin","ymin","xmax","ymax", "ausrichtung","point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma"])
    for element in list_input:
        xavg_elem = 0
        yavg_elem = 0
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        for blub in element: #get the smallest and largest x and y value for whole block
            xavg_elem += (float(blub[0]) + float(blub[2]))/2
            yavg_elem += (float(blub[1]) + float(blub[3]))/2
            if float(blub[1]) < ymin:
                ymin = float(blub[1])
                #print("y_min:",y_min)
            if float(blub[0]) < xmin:
                xmin = float(blub[0])
            if float(blub[3]) > ymax:
                ymax = float(blub[3])
            if float(blub[2]) > xmax:
                xmax = float(blub[2])
        if xmax-xmin > ymax-ymin:
            ausrichtung = 0 #horizontal
        else:
            ausrichtung = 1 #vertikal
        xavg_elem = xavg_elem/len(element)
        #print(xavg_elem)
        yavg_elem = yavg_elem/len(element)
        #element.extend([xavg_elem, yavg_elem])
        #print(element)
        #new_list.append(element)
        ##### GET CORNER POINTS
        point_xmi_ymi = [xmin,ymin]
        point_xma_ymi = [xmax,ymin]
        point_xmi_yma = [xmin,ymax]
        point_xma_yma = [xmax,ymax]
        wr.writerow([element,xmin,ymin,xmax,ymax, ausrichtung,point_xmi_ymi,point_xma_ymi,point_xmi_yma,point_xma_yma])

    resultFile.close()
    #print(new_list)
    return csv_name

def dist(rectangle1, rectangle2):
 #get minimal distance between two rectangles
    distance = 100000000


    print(rectangle1)
    for point1 in rectangle1:
        #print(point1)
        for point2 in rectangle2:
            #print(point2)
            dist = sqrt((float(point2[0]) - float(point1[0]))**2 + (float(point2[1]) - float(point1[1]))**2)
            if dist < distance:
                distance = dist

    return distance



file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
#result = order_bounding_boxes_in_each_block.get_bound_box(file)
#print(result)
#get_average_xy(result)
#rectangle1 = [[0,0],[2,0],[0,2],[2,2]]
#rectangle2 = [[3,3],[4,3],[3,4],[4,4]]
#print(compute_distance(rectangle1,rectangle2))
data = pandas.read_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv", sep=";")
data = data[["point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma"]]
data.to_csv("blub.csv", sep=",", index=False, header=None)
data_new = pandas.read_csv("blub.csv", sep=";",header=None)
data_new = data_new.to_numpy()
#print(data_new.to_string())
#print(data.loc[:])
dm = np.asarray([[dist(p1, p2) for p2 in data_new] for p1 in data_new])