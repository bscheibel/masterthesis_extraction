### FIRST READ EACH BLOCK IN AN ARRAY

from bs4 import BeautifulSoup

def get_bound_box():
    response = open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.html')
    html_doc = response.read()
    response.close()
    html_file = BeautifulSoup(html_doc, 'html.parser')

    all_elements = []
    blocks = html_file.findAll('block')
    for block in blocks:
        list_elements = []
        words = block.findAll('word')
        for word in words:
            word_list = []
            word_list.append(word["xmin"])
            word_list.append(word["ymin"])
            word_list.append(word["xmax"])
            word_list.append(word["ymax"])
            word_list.append(word.string)
            list_elements.append(word_list)
        all_elements.append(list_elements)


    #### NEXT SORT ELEMENTS IN EACH BLOCK BY THEIR X AND Y COORDINATES
    #### FIRST TRYING XMIN und YMAX
    ###FIRST CHECKING IF THE ELEMENTS ARE VERTICAL, IF YES THEN NO SORTING
    new_all_elements = []

    for element in all_elements:
        later_bigger = (float(element[-1][0])-(float(element[0][0]))) #check if xmin from first element is bigger than xmin from last element
        abstand_x = abs(float(element[-1][0])-(float(element[0][2])))
        abstand_y = abs(float(element[-1][3])-float(element[0][1]))
        if later_bigger >= -5:
            #print(abstand_x-abstand_y)
            new_all_elements.append(element)
        else:
            new_element = sorted(element, key=lambda k: [float(k[0])])
            new_all_elements.append(new_element)


    for element in new_all_elements:
        for blub in element:
            print(blub[4])

        print("\n")

    return new_all_elements