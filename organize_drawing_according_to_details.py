import order_bounding_boxes_in_each_block
import re

def get_details(result):
    #print(result)
    reg = r"([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)"
    details_ = []
    details = []
    for element in result:
        blubi = ""
        for blub in element:
            blubi += blub[4] + " "
        if re.match(reg,blubi):
            details_.append(element)



    for elem in details_:
        #print(elem)
        ymin = 100000000
        ymax = 0
        xmin = 100000000
        xmax = 0
        text = ""
        for blub in elem:
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
        details.append(list((xmin, ymin,xmax, ymax,text)))

    #print(details)
    return details


file = "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.html"
result = order_bounding_boxes_in_each_block.get_bound_box(file)
details = get_details(result)
details.sort(key= lambda x: x[0])
print(details)
sections = []

left_x = details[0][0]
right_x = details[0][2]

