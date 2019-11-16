# coding: utf8
import numpy as np
import pandas
import csv
from math import sqrt
from sklearn.cluster import DBSCAN

def get_average_xy(list_input):
    csv_name = "/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv"
    resultFile = open(csv_name, 'w')
    wr = csv.writer(resultFile, delimiter=";")
    wr.writerow(["element", "xmin","ymin","xmax","ymax", "ausrichtung","point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma"])
    result_df = pandas.DataFrame(columns=["point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma","ausrichtung"])
    for element in list_input:
        #print(len(element))
        xavg_elem = 0
        yavg_elem = 0
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        #print(element)
        newList = []
        check = False
        if len(element) == 5 and not isinstance(element[0], list):
            #print("bb")
            newList.append(element)
            #print(len(newList))
            element = newList
        """if len(element) != 5 and isinstance(element[0], list):
            for el in element:
                check = isinstance(el[0], list)
                if len(el) != 5:
                    print(el)
                #if check:
                #    print(el)"""

        for blub in element: #get the smallest and largest x and y value for whole block

            if isinstance(blub[0],list) and len(blub[0])==5:
                blub = blub [0]
            if float(blub[1]) < ymin:
                ymin = float(blub[1])
                #print("y_min:",y_min)
            if float(blub[0]) < xmin:
                xmin = float(blub[0])
            if float(blub[3]) > ymax:
                ymax = float(blub[3])
            if float(blub[2]) > xmax:
                xmax = float(blub[2])
        if float(xmax)-float(xmin) > 1.3*(float(ymax)-float(ymin)):
            ausrichtung = 0 #horizontal
        if 1.5*(float(xmax)-float(xmin)) < float(ymax)-float(ymin):
            ausrichtung = 1 #vertikal
        else:
            ausrichtung = 3 #sonstiges


        ##### GET CORNER POINTS
        point_xmi_ymi = [xmin,ymin]
        point_xma_ymi = [xmax,ymin]
        point_xmi_yma = [xmin,ymax]
        point_xma_yma = [xmax,ymax]
        wr.writerow([element,xmin,ymin,xmax,ymax, ausrichtung,point_xmi_ymi,point_xma_ymi,point_xmi_yma,point_xma_yma])
        result_df.loc[len(result_df)]=[point_xmi_ymi,point_xma_ymi, point_xmi_yma, point_xma_yma,ausrichtung]

    resultFile.close()
    #print(result_df)
    return result_df

def intersects(rectangle1, rectangle2): #using the separating axis theorem, returns true if they intersect, otherwise false
    #print(rectangle2[0])
    #for rect in rectangle1:

    rect_1_min = eval(rectangle1[0])
    rect_1_max = eval(rectangle1[3])
    rect1_bottom_left_x= rect_1_min[0]
    rect1_top_right_x=rect_1_max[0]
    rect1_bottom_left_y= rect_1_max[1]
    rect1_top_right_y= rect_1_min[1]

    rect_2_min = eval(rectangle2[0])
    rect_2_max = eval(rectangle2[3])
    rect2_bottom_left_x= rect_2_min[0]
    rect2_top_right_x=rect_2_max[0]
    rect2_bottom_left_y= rect_2_max[1]
    rect2_top_right_y=rect_2_min[1]

    return not (rect1_top_right_x < rect2_bottom_left_x or rect1_bottom_left_x > rect2_top_right_x or rect1_top_right_y > rect2_bottom_left_y or rect1_bottom_left_y < rect2_top_right_y)


def dist(rectangle1, rectangle2):
 #get minimal distance between two rectangles
    distance = 100000000
    #print(rectangle1)
    for point1 in rectangle1[:4]:
        point1 = eval(point1)
        #print(point1)
        for point2 in rectangle2[:4]:
            #print(point2)
            point2 = eval(point2)
            #dist1 = (float(point2[0]) - float(point1[0])) + ((float(point2[1]) - float(point1[1])))
            dist = sqrt(((float(point2[0]) - float(point1[0])))**2 + ((float(point2[1]) - float(point1[1])))**2)
            #print(dist)
            if dist < distance:
                distance = dist
        if rectangle1[4] != rectangle2[4]:
            distance = dist + 100
        #print(intersects(rectangle1,rectangle2))
        if intersects(rectangle1, rectangle2):
            distance = 0
            #print(rectangle1)
    return distance

def clustering(dm,eps):
    db = DBSCAN(eps=eps, min_samples=1, metric="precomputed").fit(dm)                                                                                        ##3.93 until now, bei 5 shon mehr erkannt, 7 noch mehr erkannt aber auch schon zu viel; GV12 ist 4.5 gut für LH zu wenig
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    data_df = pandas.read_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv", sep=";")
    data_df["cluster"] = labels
    data_df.groupby(['cluster', 'ausrichtung'])['element'].apply(','.join).reset_index().to_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/values_clusteredfrom_precomputed_dbscan.csv",sep=";", header=False, index=False)
    return data_df

def cluster_and_preprocess(result,eps):
    result = get_average_xy(result) #input: array of arrays, output: either csv file or array of arrays

    #data = pandas.read_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv", sep=";")
    #data = data[["point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma","ausrichtung"]]
    result.to_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/blub.csv", sep=";", index=False, header=None)
    with open('/home/bscheibel/PycharmProjects/dxf_reader/temporary/blub.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        result = list(readCSV)

    dm = np.asarray([[dist(p1, p2) for p2 in result] for p1 in result])
    clustering_result = clustering(dm,float(eps))
    return clustering_result

