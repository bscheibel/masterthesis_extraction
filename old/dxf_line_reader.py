
def printpoint(b):
    print(b)
    obj = dict(zip(b[::2], b[1::2]))
    try:
        if obj['100'] == 'AcDbMText':
            print('{}'.format(obj['0']))
    except:
        pass

buffer = ['0', 'fake']
filepath = 'GV_12.DXF'
with open(filepath,'r', errors="replace") as fp:
    line = fp.readline()
    cnt = 1
    #while line:
        #line = fp.readline()
    #line = line.rstrip()
    print(line)
    if line == '0':  # we've started a new section, so
        print("Line {}: {}".format(cnt, line.strip()))
            #try:
            #    printpoint(buffer)  # handle the captured section
            #except:
            #    print("ERROR")

    #buffer = []  # and start a new one
    #buffer.append(line)
    cnt += 1
#f.close()

#printpoint(buffer)        # buffer left over from last pass through loop

#https://leancrew.com/all-this/2016/12/dxf-data-extraction/