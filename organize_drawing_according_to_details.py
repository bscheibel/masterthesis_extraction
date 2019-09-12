import order_bounding_boxes_in_each_block
import re
from math import sqrt

def get_details(result): #search for all details in drawing and store it in list details, first need to append all text elements of one line and then check if regular expression is found in this text element
    reg = r"([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)"
    details_ = []
    for element in result:
        new_arr = ""
        for x in element:
            new_arr += x[4] + " "
        if re.match(reg,new_arr):
            details_.append(element)

    details = []
    xbiggest = 0
    ybiggest = 0
    for elem in details_: #now go to newly created list of all details and get the min and max coordinates of the respective bbox around the detail
        #print(elem)
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        text = ""
        for ele in elem: #check if coordinates are bigger or smaller
            text += ele[4]
            #print(text)
            if float(ele[1]) < ymin:
                ymin = float(ele[1])
                # print("y_min:",y_min)
            if float(ele[0]) < xmin:
                xmin = float(ele[0])
            if float(ele[3]) > ymax:
                ymax = float(ele[3])
            if float(ele[2]) > xmax:
                xmax = float(ele[2])
        details.append(list((xmin, ymin,xmax, ymax,text))) # create new list with the textual details and the min and max coordinates of these details
        number = len(details)

    if ymax > ybiggest:  ###get biggest x and y values
        ybiggest = ymax
    if xmax > xbiggest:
        xbiggest = xmax

    #print(details)
    return details, number, ybiggest, xbiggest


file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
result = order_bounding_boxes_in_each_block.get_bound_box(file)
details, number, ybiggest, xbiggest = get_details(result)
#details = sorted(details, key=lambda x: sqrt((x[0] - 0)**2 + (x[1] - 0)**2)) #sort by distance from 0,0
details = sorted(details, key=lambda x: x[0]) #sort by distance from 0,0

#print(details, number)

sections = []
for first in details:
    x_min = -1
    y_min = -1
    x_max = -1
    y_max = -1
    firstx_max = first[2]
    firstx_min = first[0]
    firsty_max = first[3]
    firsty_min = first[1]

    distance_xmax = 100000000000
    distance_xmin = 100000000000
    distance_ymin = 100000000000
    distance_ymax = 100000000000

    for second in details:
        secondx_min = second[0]
        secondx_max = second[2]
        secondy_min = second[1]
        secondy_max = second[3]

        if secondx_max < firstx_min and abs(firsty_min-secondy_min) < 90 and first != second:  ###check for left side, are there any other details at the left side at a certain y-span
            #print(first,second)
            if abs(firstx_min - secondx_max)/2 < distance_xmax:
                distance_xmax = abs(firstx_min - secondx_max)/2
                x_min = secondx_max + distance_xmax
        if secondx_min > firstx_max and abs(firsty_min-secondy_min) < 190 and first != second: ####check for right side
            if abs(secondx_min - firstx_max)/2 < distance_xmin:
                #print(first, second)
                distance_xmin = abs(secondx_min - firstx_max)/2
                x_max = firstx_max + distance_xmin
        if firsty_min > secondy_max and abs(firstx_min-secondx_min) < 40 and first != second: ####check above
            if abs(firsty_min - secondy_max)/2 < distance_ymin:
                #print(first, second)
                distance_ymin = abs(firsty_min - secondy_max)/2
                y_min = firsty_min
        if firsty_max < secondy_min and abs(firstx_min-secondx_min) < 40 and first != second: ####check below
            if abs(firsty_max - secondy_min)/2 < distance_ymax:
                #print(first, second)
                distance_ymax = abs(firsty_max - secondy_min)/2
                y_max = secondy_min

    if y_min == -1:
        y_min = firsty_min
    if x_min == -1:
        x_min = 0
    if x_max == -1:
        x_max = firstx_max + distance_xmax
    if y_max == -1:
        y_max = 1000000000
    sections.append((first,x_min, y_min,x_max,y_max))

for section in sections:
    print(section)