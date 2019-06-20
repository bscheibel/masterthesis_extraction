def printsection(b):
    print(b)
    obj = dict(zip(b[::2], b[1::2]))
    for keys, values in obj.items():
        if keys == '1':
            print(values)
            print("\n")

    #if obj.get('1'):
    #    print('{}'.format(obj['1']))


buffer = []
file = open("GV_12.DXF", "r")
for line in file:
    line = line.strip()
    #print(line)
    if line == '100':         # we've started a new section, so
        printsection(buffer)      # handle the captured section
        buffer = []             # and start a new one
    buffer.append(line)
printsection(buffer)