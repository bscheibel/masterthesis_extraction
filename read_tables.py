import tabula


#tables = tabula.read_pdf("iso_documents/ISO1101.PDF", multiple_tables=True)
#for table in tables:
#    print(table)

#pdftotext - layout!!!!

tabula.convert_into("iso_documents/ISO1101.PDF", "output.csv", output_format="csv", pages='all', multiple_tables=True)
df = tabula.read_pdf("iso_documents/ISO1101.PDF", pages='all', multiple_tables=True)
print(df)