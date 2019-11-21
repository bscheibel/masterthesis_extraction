# coding=utf8
import re


def print_clean(dims): ##alles raus was nicht relevant ist! und zeichen ersetzen!
    dims_new = {}
    reg_clean = r"[a-zA-Z]{4,}|^\d\s\d$|^[a-zA-Z]{2,}\d.*$|^[A-Z]{1}$|^mm$|^\d{2}\.\d{2}\.\d{4}|^-$|A\d|^\d{1}$|^[A-Za-z]{3,}\.?$|^\d{5}|^\d{1}\s\W\s\d"
    for dim in dims:
        if re.search(reg_clean, dim):
            continue
        else:
            coords = dims[dim]
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
            reg12 = re.compile(r"(.*\d{1,4}\W?\d{0,4})\s?\+\s-\s?(\d{1,4}\W?\d{0,4})\s?(\d{1,4}\W?\d{0,3})") ##???? was machst du?? nach toleranzen suchen, mit +/- blabla
            reg13 = re.compile(r"(.*)\+\s\+\s(\d*\W\d*)\s(\d*\W\d*)(.*)")
            reg14 = re.compile(r"(\+\s?\d*,?.?\d*)\s*(\d*,?.?\d*)\s*(\+?\s?\-?\s?\d*,?.?\d*)")
            g = re.search(reg12, dim)
            f = re.search(reg13, dim)
            e = re.search(reg14, dim)
            if g:
                dim = re.sub(reg12, g.group(1) + " +" + g.group(2) + " -" + g.group(3), dim) # +/- toleranzen schön darstellen
                #print(dim)
            elif f:
                dim = f.group(1) + "+" + f.group(2) + " +" + f.group(3) + f.group(4)
            elif e:
                dim = e.group(2) + " " + e.group(1) + " " + e.group(3)

            dim = dim.replace(" ,",".").replace(", ",".").replace(",",".")
            dims_new[dim] = coords

    #for dim in dims_new:
    #    print(dim)
    #print(dims_new)
    return dims_new