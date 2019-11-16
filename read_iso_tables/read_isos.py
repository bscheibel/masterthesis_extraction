import nltk
import re
from tika import parser
einleitung = False
raw = parser.from_file('/home/bscheibel/PycharmProjects/dxf_reader/iso_documents/ISO2768-1.PDF')
#raw = parser.from_file('iso_documents/ISO286-2.PDF')
print(raw['content'])
#text = raw['content']
#sent_text = nltk.sent_tokenize(text)
#tokenized_text = nltk.word_tokenize(sent_text.split)
#tagged = nltk.pos_tag(tokenized_text)
#match = text.concordance('Toleranz')
#for text in sent_text:
#    if "Toleranz" in text and einleitung is True:
#        print(text)
#    if "Einleitung" in text:
#        einleitung = True


import subprocess
#subprocess.check_output(['ls','-l']) #all that is technically needed...
cmd = 'pdftotext -layout "/home/bscheibel/PycharmProjects/dxf_reader/iso_documents/ISO8015.PDF"'
print(subprocess.Popen(cmd, shell=True))

#convert iso document to text
text = "iso_documents/ISO8015.txt"
#search for table of content with regex
contents = []
regex = r"(.*?)[\W]+(\d+)(?=\n|$)"
r"([^\.]\d\.?\d?\.?\d?\.?\d?)\s([a-zA-Z]*)\s([a-zA-Z]*)\s*([a-zA-Z]*)\W?\s*([a-zA-Z]+)\s*\.{10,}([\d]+)"
matches = re.finditer(regex, text, re.MULTILINE)
#contents = re.findall(r"(.*?)[\W]+(\d+)(?=\n|$)", text, flags=re.M)
#print(contents)
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))
#only search for sections with toleranzen/abmaße

