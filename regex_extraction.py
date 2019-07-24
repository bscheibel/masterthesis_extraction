# coding=utf8
import re

regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)"
extracted_dimensions = []
file=open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.txt', 'r')
text= file.read()
file.close()
matches = re.findall(regex, text, re.MULTILINE)
for match in matches:
        extracted_dimensions.append(match.strip())


print(extracted_dimensions)
