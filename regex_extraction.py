# coding=utf8
import re

regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)"
regex1 = r"([A-Z]\s?\W\s?\d\d?\s?\s?\W\s?\d\d?\s?\W)" #ti get the bezeichnungen raus
regex2= r"([a-zA-Z]{3,})" #alle wörter raus???
extracted_dimensions = []
file=open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.txt', 'r')
text= file.read()
file.close()
matches = re.findall(regex, text, re.MULTILINE)
for match in matches:
        extracted_dimensions.append(match.strip())



print(extracted_dimensions)
