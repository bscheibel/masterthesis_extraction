# coding=utf8
import re

regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)" #alle gruppen von zahlen raus
regex1 = r"([A-Z]\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)" #ti get the bezeichnungen raus
regex2= r"([a-zA-Z]{3,})" #alle wörter raus???
regex_isos = r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?)" #get iso standards
reg = r"(^\d{1}$)" #einzelne Zahlen raus
reg1 = r"(^[A-Z]-?[A-Z]?$)" #einzelne Buchstaben raus
extracted_dimensions = []
file = open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.txt', 'r')
text = file.read()
file.close()
matches = re.findall(regex, text, re.MULTILINE)
for match in matches:
        extracted_dimensions.append(match.strip())
isos = []
new_dims = []
#next part replaces everything you do not need with whitespace
for dim in extracted_dimensions:
        if re.search(regex_isos, dim):
                match = re.findall(regex_isos,dim)
                isos.append(match[0])
                dim = re.sub(regex_isos,'' ,dim)
        if re.search(regex1, dim):
                dim = re.sub(regex1, '', dim)
        if re.search(regex2, dim):
                dim = re.sub(regex2,'' ,dim)
        if re.search(reg, dim):
                dim = re.sub(reg,'' ,dim)
        if re.search(reg1, dim):
                dim = re.sub(reg1,'' ,dim)
        if dim != '':
                new_dims.append(dim)

print(isos)
for dim in new_dims:
        if b:
                print("Rechtwinkligkeit")
                print(dim)
        if g:
                print("Zylinderform")
                print(dim)
        if f:
                print("Parallelität")
                print(dim)
        if c:
                print("Zylinderform")
                print(dim)
        if r:
                print("Konzentrizität oder Durchmesser?")
                print(dim)
        if i:
                print("Symmetrie")
                print(dim)
        if j:
                print("Ortstoleranz/Mittelpunkt")
                print(dim)
        if n:
                print("Durchmesser")
                print(dim)
        if É:
                print("Modifikator")
                print(dim)
        ####nicht dabei: neigungswinkel und lauftoleranzen
        if R:
                print("Radius")

        if °:
                print("Grad")

