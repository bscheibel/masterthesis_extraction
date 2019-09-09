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
    for elem in details_: #now go to newly created list of all details and get the min and max coordinates of the respective bbox around the detail
        #print(elem)
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        text = ""
        for blub in elem: #check if coordinates are bigger or smaller
            text += blub[4]
            #print(text)
            if float(blub[1]) < ymin:
                ymin = float(blub[1])
                # print("y_min:",y_min)
            if float(blub[0]) < xmin:
                xmin = float(blub[0])
            if float(blub[3]) > ymax:
                ymax = float(blub[3])
            if float(blub[2]) > xmax:
                xmax = float(blub[2])
        details.append(list((xmin, ymin,xmax, ymax,text))) # create new list with the textual details and the min and max coordinates of these details
        number = len(details)

    #print(details)
    return details, number


file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
result = order_bounding_boxes_in_each_block.get_bound_box(file)
details, number = get_details(result)
details = sorted(details, key=lambda x: sqrt((x[0] - 0)**2 + (x[1] - 0)**2)) #sort by distance from 0,0
print(details, number)



sections = []
max_x_last_element = 0
max_y_last_element = 0
border = 0
i = 0
overlapping = []
for x in details:
    min_x = x[0]
    #print(min_x)
    if max_x_last_element != 0: #start compare second and first element #check if min_x of new element is bigger than max_x of last element to see if they overlap in their xs
        distance = min_x - max_x_last_element
        if distance < 0: #if they overlap then there has to be segmentation of y as well
            print("überschneidend")
            ov = []
            ov.append((x[0],))
            ov.append(details[i-1])
            ov = sorted(ov, key=lambda x: x[1])
            print(ov)
            y_lower_min = ov[1][1]
            print(y_lower_min)
            sections.append(details[i-1][x])


            overlapping.append((x,details[i-1]))

        #print(distance)
        else:
            border_x = max_x_last_element+(distance/2)
            sections.append((border_x, 100000000))
    max_x_last_element = x[2]
    i += 1

#print(overlapping)

"""
for y in details:
    min_y = y[1]
    if max_y_last_element != 0:
        distance = min_y - max_y_last_element
        border_y = max_y_last_element + (distance/2)
        sections_y.append(border_y)
    max_y_last_element = y[3]

print(sections_y)"""

#oben,links beginnen