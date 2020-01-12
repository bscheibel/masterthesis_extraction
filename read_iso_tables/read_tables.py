import tabula
import camelot
import subprocess
import re

#tables = tabula.read_pdf("iso_documents/ISO2768-1.PDF", pages=3)
#for table in tables:
#    print(table)

#pdftotext - layout!!!!

#tabula.convert_into("iso_documents/ISO2768-1.PDF", "output_mit_tabula.csv", output_format="csv", pages='all', multiple_tables=True)
#df = tabula.read_pdf("iso_documents/ISO1101.PDF", pages='all', multiple_tables=True)
#print(df)

def file_read(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line.strip().replace(" ",""))
        print(content_array)


#file_read('drawings/5129275_Rev01-GV12.txt')
tables = camelot.read_pdf("/home/bscheibel/PycharmProjects/engineering_drawings_extraction/iso_documents/ISO2768-1.PDF", pages="3")
tables.export('output_mit_camelot.csv', f='csv')

output = subprocess.check_output(["less","/home/bscheibel/PycharmProjects/engineering_drawings_extraction/iso_documents/ISO2768-1.PDF"])
print(output)

re_data_prefix = re.compile("^[0-9]+[.].*$")
re_data_fields = re.compile("(([^ ]+[ ]?)+)")
for line in output.splitlines():
    if re_data_prefix.match(line):
        for l in re_data_fields.findall(line):
            print[l[0].strip()]
