import numpy as np
import pandas
import csv
from math import sqrt
from sklearn.cluster import DBSCAN
from sklearn.cluster import OPTICS
import order_bounding_boxes_in_each_block

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
        if float(xmax)-float(xmin) > 1.5*(float(ymax)-float(ymin)):
            ausrichtung = 0 #horizontal
            print("horizontal")
        if 1.5*(float(xmax)-float(xmin)) < float(ymax)-float(ymin):
            ausrichtung = 1 #vertikal
            print("vertikal")
        else:
            ausrichtung = 3 #sonstiges
            print("sonstiges")
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

def intersects(self, other):
    return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)

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
            #print(rectangle2[4], "- ", rectangle1[4])
    return distance

def clustering(distance_matrix):
    db = DBSCAN(eps=0.0001, min_samples=1, metric="precomputed").fit(dm)  ##3.93 until now, bei 5 shon mehr erkannt, 7 noch mehr erkannt aber auch schon zu viel; GV12 ist 4.5 gut für LH zu wenig
    #db = OPTICS(min_samples=1,xi=0.1, metric="precomputed").fit(dm)
    labels = db.labels_
    # Number of clusters in labels
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    data_df = pandas.read_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv",
                           sep=";")
    data_df["cluster"] = labels
    data_df.groupby('cluster')['element'].apply(' '.join).reset_index().to_csv("values_clusteredfrom_precomputed_dbscan.csv",sep=";")


#file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.html"
file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
result = order_bounding_boxes_in_each_block.get_bound_box(file)
print(result)
"""get_average_xy(result)
#rectangle1 = [[450,286],[464,286],[450,376],[464,376]]
#rectangle2 = [[450,316],[456,316],[450,329],[456,329]]
#print(dist(rectangle1,rectangle2))
data = pandas.read_csv("/home/bscheibel/PycharmProjects/dxf_reader/temporary/list_to_csv_with_corner_points.csv", sep=";")
data = data[["point_xmi_ymi","point_xma_ymi","point_xmi_yma","point_xma_yma","ausrichtung"]].replace("'","")
#print(data)
data.to_csv("blub.csv", sep=";", index=False, header=None)
result = []
with open('blub.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    result = list(readCSV)

dm = np.asarray([[dist(p1, p2) for p2 in result] for p1 in result])
#print(dm)
clustering(dm)"""