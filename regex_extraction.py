# coding=utf8
import re

def clean(extracted_dimensions):
    #next part extracts the isos and removes everything we dont need like just text or the X:X stuff, einzelne buchstaben und zahlen
    for dim in extracted_dimensions:
        if re.match(regex_isos, dim): #isos
            match = re.findall(regex_isos,dim)
            isos.append(match[0])
            extracted_dimensions.remove(dim)


    for dim in extracted_dimensions:
        match =re.match(reg_all, dim)
        if match:
            #print(re.findall(reg_all,dim))
            #print(match[0])
            try:
                extracted_dimensions.remove(dim)
            except:
                print("error")

    #print(isos)
    #print(extracted_dimensions)
    return isos, extracted_dimensions


def print_clean(extracted_dimensions):
    for dim in extracted_dimensions:
        if "b" in dim:
            print("Rechtwinkligkeit")
            print(dim)
        if "g" in dim:
            print("Zylinderform")
            print(dim)
        if "f" in dim:
            print("Parallelität")
            print(dim)
        if "c" in dim:
            print("Zylinderform")
            print(dim)
        if "r" in dim:
            print("Konzentrizität?")
            print(dim)
        if "i" in dim:
            print("Symmetrie")
            print(dim)
        if "j" in dim:
            print("Ortstoleranz/Mittelpunkt")
            print(dim)
        if "n" in dim:
            print("Durchmesser")
            print(dim)
        if "É" in dim:
            print("Modifikator")
            print(dim)
        ####nicht dabei: neigungswinkel und lauftoleranzen
        if "R" in dim:
            print("Radius")
            print(dim)
        if "°" in dim:
            print("Grad")
        if "Ø" in dim:
            print("Durchmesser")

regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)" #alle gruppen von zahlen raus
regex1 = r"([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)" #ti get the bezeichnungen raus
regex2 = r"((?!\d)(?!Rpk)[a-zA-Z]{3,})" #alle wörter raus??? außer Rpk
regex_isos = r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?)" #get iso standards
reg = r"(^\d{1}$)" #einzelne Zahlen raus #checked
reg1 = r"(^[A-Z]{1}-?[A-Z]?$)" #einzelne Buchstaben raus #checked
reg_all = r"(^(?!0)\d{1}$)|(^[A-Z]{1}-?[A-Z]?$)|(^[A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)|((?!\d)(?!Rpk)[a-zA-Z]{3,})"
extracted_dimensions = []
file = open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.txt', 'r')
text = file.read()
file.close()
matches = re.findall(regex, text, re.MULTILINE)
for match in matches:
    extracted_dimensions.append(match.strip())
#print(extracted_dimensions)
isos = []
isos, dims = clean(extracted_dimensions)
#print(isos)
#dims = clean(dims)
for dim in dims:
    print(dim)
print_clean(dims)