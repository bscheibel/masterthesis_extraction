import re
reg_all = re.compile(r"(^[A-Z]{1}-?[A-Z]?\s*$)|([A-Z]\W?[A-Z]?\s?\W\s?\d\d?\s?\s?:\s?\d\d?\s?\W)|((?!\d)(?!Rpk)[a-zA-Z]{3,}?\W)|(?!0)(^\d{1}\s*$|A\d{1}|\d/\d)")
regex = r"(\S+\s{1,3}?\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s?\S*\S*\s+)"
file = open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.txt', 'r')
text = file.read()
file.close()
extraction = []
matches = re.findall(regex, text, re.MULTILINE)
for match in matches:
    #print(match)
    extraction.append(match.strip())
i = 0
new_matches = []
for match in extraction:
    #print(match)
    #print("blub")
    match = match.split('\n')[0]
    #if len(match)>1:
    #    extraction.append(match[1])
        #print(match[1])
    #print([match])
    if not re.search(reg_all, match):
        #print("blub")
        new_matches.append(match)
    i += 1

print(new_matches)