#!/usr/bin/env python

#from fileinput \
import fileinput


def printpoint(b):
    print(b)
    obj = dict(zip(b[::2], b[1::2]))
    if obj['0'] == 'AcDbMText':
        print('{}'.format(obj['0']))


print('Code','Text')# header line
buffer = ['0', 'fake']    # give first pass through loop something to process
for line in fileinput.input("GV_12.DXF", errors="replace"):
    line = line.rstrip()
    print(line)
    if line == '0':         # we've started a new section, so
        printpoint(buffer)      # handle the captured section
        buffer = []             # and start a new one
    buffer.append(line)

printpoint(buffer)        # buffer left over from last pass through loop
