import order_bounding_boxes_in_each_block
import re
import csv
import camelot
from math import sqrt

def get_details(result): #search for all details in drawing and store it in list details, first need to append all text elements of one line and then check if regular expression is found in this text element
    reg = r"([A-Z])-\1|([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)"
    details_ = []
    for element in result:
        new_arr = ""
        for x in element:
            new_arr += x[4] + " "
        if re.match(reg,new_arr):
            #print(new_arr)
            details_.append(element)

    details = []
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

    #print(details)
    return details, number

#print(details, number)

def get_borders(details, coords):
    sections = []
    print(coords)
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
            for table in coords:
                print(table)
                if table[0] <= x_min and table[2] >= x_max:
                    y_max = table[1]
                    print("BLUB", y_max)
                    break
                else:
                    y_max = 1000000000
        sections.append((first,x_min, y_min,x_max,y_max))

    for section in sections:
        print(section)
    return sections

def intersects(detail, rectangle): #using the separating axis theorem
    #print(detail)


    rect1_bottom_left_x = detail[1][0]
    rect1_top_right_x = detail[1][2]
    rect1_bottom_left_y = detail[1][3]
    rect1_top_right_y = detail[1][1]

    rect2_bottom_left_x = float(rectangle[0][0])
    rect2_top_right_x = float(rectangle[0][2])
    rect2_bottom_left_y = float(rectangle[0][3])
    rect2_top_right_y = float(rectangle[0][1])


    return not (rect1_top_right_x < rect2_bottom_left_x or rect1_bottom_left_x > rect2_top_right_x or rect1_top_right_y > rect2_bottom_left_y or rect1_bottom_left_y < rect2_top_right_y)

def table_intersects(detail, rectangle): #everything that is under the y coordinates of the tables
    #print(detail[4])


    table_bottom_left_x = detail[0]
    table_top_right_x = detail[2]
    table_bottom_left_y = detail[3]
    table_top_right_y = detail[1]

    rect_bottom_left_x = float(rectangle[0][0])
    rect_top_right_x = float(rectangle[0][2])
    rect_bottom_left_y = float(rectangle[0][3])
    rect_top_right_y = float(rectangle[0][1])

    if "REV." in detail[4]:
        #print(detail)
        return (rect_bottom_left_y >= table_top_right_y and (rect_top_right_x >= table_bottom_left_x))

    else:
        return(rect_bottom_left_y > table_top_right_y and (rect_bottom_left_x >= table_bottom_left_x and rect_bottom_left_x <= table_top_right_x))


def get_table_coords(result):
    coords = []
    #tables = camelot.read_pdf(file,spreadsheet=True, area=(50,50,50,50), relative_area=True) ##did not work
    #print(tables[0]._bbox)
    reg = r"(All dimensions\D*)|(REV\.)"
    details_ = []
    for element in result:
        new_arr = ""
        for x in element:
            new_arr += x[4] + " "
        if re.match(reg,new_arr):
            #print(element)
            details_.append(element)

    details = []
    for elem in details_: #now go to newly created list of all details and get the min and max coordinates of the respective bbox around the detail
        #print(elem)
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        text = ""
        for ele in elem: #check if coordinates are bigger or smaller
            text += ele[4] + " "
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
    #for det in details:
    #    print(det, number)

    return number,details

def remove_tables(tables, result):
    result_array = []
    #print(tables)
    for res in result:
        overlaps = False
        for det in tables:
            if table_intersects(det,res):
                overlaps = True
        if not overlaps:
            result_array.append(res)
            #else:
            #    print("NOT:", res)

    #for res in result_array:
    #    print(res)
    return result_array


file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
#file2 = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.pdf"
#file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.html"
result = order_bounding_boxes_in_each_block.get_bound_box(file)
#print(result)
details, number= get_details(result)
number, coords = get_table_coords(result)
result = remove_tables(coords, result)
#print(details)
#details = sorted(details, key=lambda x: sqrt((x[0] - 0)**2 + (x[1] - 0)**2)) #sort by distance from 0,0
details = sorted(details, key=lambda x: x[0]) #sort by distance from 0,0
sections = get_borders(details, coords)
section = []

#print(new_result)

for sect in sections:
    coord_name = sect[0][4]
    coord = (sect[1:])
    section.append((coord_name,coord))


with open("section.csv", "w") as writeFile:
    writer = csv.writer(writeFile)
    for det in section:
        writer.writerows(det)
        for res in result:
            if intersects(det,res):
                writer.writerows(res)
        writer.writerows("\n")


writeFile.close()

###alles durchgehen und zu jeweiligen details zuordnen
