# from tika import parser
#
# raw = parser.from_file("GV_12.pdf")
# raw = str(raw)
#
# safe_text = raw.encode('utf-8', errors='ignore')
#
# #safe_text = str(safe_text).replace("\n", "").replace("\\", "")
# print('--- safe text ---' )
# print(safe_text
#
# )


import textract
text = textract.process("GV_12.pdf")