import camelot
import matplotlib.pyplot as plt
tables = camelot.read_pdf('/Users/beatescheibel/PycharmProjects/dxf_reader/iso_documents/ISO2768-1.PDF', pages="3",line_scale=70, line_tol=2, joint_tol=35)
tables.export('foo.csv', f='csv')
print(tables[0].df)
camelot.plot(tables[0], kind='grid')
plt.show()