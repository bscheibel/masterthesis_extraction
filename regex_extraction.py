# coding=utf8
import re
import pandas

def clean(extracted_dimensions):
    #next part extracts the isos and removes everything we dont need like just text or detail/maßstab, einzelne buchstaben und zahlen
    isos = []
    for line in extracted_dimensions:
        matches = re.findall(regex_isos,line)
        for match in matches:
            isos.append(match)


    i = 0
    new_matches = []
    for match in extracted_dimensions:
        match = match.split('\n')[0]
        if not re.search(reg_all, match):
            new_matches.append(match)
        i += 1

    #print(isos)
    #print(extracted_dimensions)
    return isos, new_matches


def print_clean(dims):
    dims_new = []
    dimss = []
    for dim in dims:
        dim = re.split("CT",dim)
        dimss.extend(dim)
    #print(dimss)
    for dim in dimss:
        if re.search(r"b\s\d*\W?\d*\s.",dim):
            dim = dim.replace('b', u"\u27C2")
        if re.search(r"g\s\d*\W?\d*", dim):
            dim = dim.replace('g', u"\u232D")
        if re.search(r"f\s\d*\W?\d*", dim):
            dim = dim.replace('f',  u"\u2225")
        if re.search(r"r\s\d*\W?\d*", dim):
            dim = dim.replace('r', u"\u25CE")
        if re.search(r"i\s\d*\W?\d*", dim):
            dim = dim.replace('i', u"\u232F")
        if re.search(r"j\s\d*\W?\d*", dim):
            dim = dim.replace('j', u"\u2316")
        if re.search(r"d\s\d*\W?\d*", dim):
            dim = dim.replace('d', u"\u2313")
        if re.search(r"c\s+\d*", dim):
            dim = dim.replace('c', u"\u23E5")
        if re.search(r"n\s+\d*", dim):
            dim = dim.replace('n', u"\u2300")
        if "È" in dim:
            dim = dim.replace('È', 'GG')
        if "`" in dim:
            dim = dim.replace('`', u"\u00B1")
        if "#" in dim:
            dim = dim.replace('#', "↔")
        if "⌀" in dim:
            dim = dim.replace('⌀', "Ø")
        reg12 = re.compile(r"(\d{1,2}\.?\d{0,2})\s\+\s-\s(\d{1,2}\.?\d{0,2})\s(\d{1,2}\.?\d{0,2})")
        g = re.search(reg12, dim)
        if g:
            dim = re.sub(reg12, g.group(1) + " + " + g.group(2) + " - " + g.group(3), dim)
        dims_new.append(dim.strip())
        dimms = []
        i = 0
        for dim in dims_new:
            last_item = i - 1
            next_item = i + 1
            if not re.search(r"[a-zA-Z]{3,}|^\d\s\d$|^[a-zA-Z]{2,}\d.*$",dim):
                dimms.append(dim)


        ####nicht dabei: neigungswinkel und lauftoleranzen

    return dimms



regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)" #alle gruppen von zahlen raus
regex1 = r"([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)" #ti get the bezeichnungen raus
regex2 = r"((?!\d)(?!Rpk)[a-zA-Z]{3,})" #alle wörter raus??? außer Rpk
regex_isos = r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?)|(EN\s\d*)" #get iso standards
reg = r"(^\d{1}$)" #einzelne Zahlen raus #checked
reg1 = r"(^[A-Z]{1}-?[A-Z]?$)" #einzelne Buchstaben raus #checked
reg_all = re.compile(r"(ISO\s\d\d\d\d?\W?\d?\W?\d?\W?\d?|(EN\s\d*)|^[A-Z]{1}-?[A-Z]?\s*$)|([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)|((?!\d)(?!Rpk)[a-zA-Z]{3,}?\W)|(?!0)(^\d{1}\s*$|A\d{1}|\d\s\d\s\d\s\d\s\d)|BY|to:?|of|or|is|in|as|be|by |\d\d\d\d\d\d\d|\d\s\/\s\d")
extracted_dimensions = []
#text = csv_to_text.read_csv('/home/bscheibel/PycharmProjects/dxf_reader/temporary/text_merged_GV12.csv')

file = open('text_merged.csv', 'r')
#text = file.read()
#file.close()
text_df = pandas.read_csv(file)
text = text_df['Text']
#print(text)
#matches = re.findall(regex, text, re.MULTILINE)
for line in text:
    extracted_dimensions.append(line.strip())

isos, dims = clean(extracted_dimensions)
#print(isos)
isos, dims = clean(dims)
new_dims = print_clean(dims)
for dim in new_dims:
    print(dim)