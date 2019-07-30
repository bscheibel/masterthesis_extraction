# coding=utf8
import re
import csv_to_pandadf

def clean(extracted_dimensions):
    #next part extracts the isos and removes everything we dont need like just text or detail/maßstab, einzelne buchstaben und zahlen
    for dim in extracted_dimensions:
        if re.match(regex_isos, dim): #isos
            match = re.findall(regex_isos,dim)
            isos.append(match[0])
            extracted_dimensions.remove(dim)

    i = 0
    new_matches = []
    for match in extracted_dimensions:
        # print(match)
        match = match.split('\n')[0]
        # if len(match)>1:
        #    extraction.append(match[1])
        # print(match[1])
        if not re.search(reg_all, match):
            new_matches.append(match)
        i += 1

    #print(isos)
    #print(extracted_dimensions)
    return isos, new_matches


def print_clean(dims):
    mal = "no"
    vorzeichen = "no"
    for dim in dims:
        if re.match(r"b\s\d*\W?\d*\s.",dim):
            print("Rechtwinkligkeit")
            print(dim)
            continue
        if re.match(r"g\s\d*\W?\d*", dim):
            print("Zylinderform")
            print(dim)
            continue
        if re.match(r"g\s\d*\W?\d*", dim):
            print("Parallelität")
            print(dim)
            continue
        if re.match(r"g\s\d*\W?\d*", dim):
            print("Zylinderform")
            print(dim)
            continue
        if re.match(r"g\s\d*\W?\d*", dim):
            print("Konzentrizität")
            print(dim)
            continue
        if re.match(r"i\s\d*\W?\d*", dim):
            print("Symmetrie")
            print(dim)
            continue
        if re.match(r"j\s\d*\W?\d*", dim):
            print("Ortstoleranz/Mittelpunkt")
            print(dim)
        if re.match(r"n\d*", dim):
            print("Durchmesser")
            print(dim)
        if "É" in dim:
            print("Modifikator")
            print(dim)
            continue
        ####nicht dabei: neigungswinkel und lauftoleranzen
        if re.match(r"R\d*$",dim):
            print("Radius")
            print(dim)
            continue
        if "°" in dim:
            print("Grad")
            print(dim)
            continue
        if re.match(r"Ø\s*\d*\W?\d*", dim):
            print("Durchmesser")
            print(dim)
            continue

def merge(dims):
    last_item = ""
    i = 0
    new_dims = []
    for dim in dims:
        dims[i] = dim.replace('È','GG')
        if re.match(r"\d?x$", last_item):
            last_item = last_item + " " + dims[i]
        if re.match(r"R0", dim):
            last_item = dim + last_item
        if re.match(r"^°$", last_item):
            last_item = dim + last_item
        new_dims.append(last_item)
        i += 1
        last_item = dim
    return dims


regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)" #alle gruppen von zahlen raus
regex1 = r"([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)" #ti get the bezeichnungen raus
regex2 = r"((?!\d)(?!Rpk)[a-zA-Z]{3,})" #alle wörter raus??? außer Rpk
regex_isos = r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?)" #get iso standards
reg = r"(^\d{1}$)" #einzelne Zahlen raus #checked
reg1 = r"(^[A-Z]{1}-?[A-Z]?$)" #einzelne Buchstaben raus #checked
reg_all = re.compile(r"(^[A-Z]{1}-?[A-Z]?\s*$)|([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)|((?!\d)(?!Rpk)[a-zA-Z]{3,}?\W)|(?!0)(^\d{1}\s*$|A\d{1}|\d/\d)")
extracted_dimensions = []


text = csv_to_pandadf.read_csv('/home/bscheibel/PycharmProjects/dxf_reader/temporary/text_merged_GV12.csv')

"""file = open('/home/bscheibel/PycharmProjects/dxf_reader/temporary/text_merged.csv', 'r')
text = file.read()
file.close()
matches = re.findall(regex, text, re.MULTILINE) """
for match in text:
    extracted_dimensions.append(match.strip())
#print(extracted_dimensions)
"""for dim in extracted_dimensions:
    print( [dim] )"""
isos = []
isos, dims = clean(extracted_dimensions)
for dim in dims:
   print(dim)
#print(isos)
new_dims = []
new_dims = merge(dims)
print(new_dims)

#print_clean(dims)