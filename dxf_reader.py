#!/usr/bin/env python

from fileinput import input


def printpoint(b):
    print(b)
    obj = dict(zip(b[::2], b[1::2]))
    if obj['0'] == 'AcDbMText':
        print('{}'.format(obj['100']))


print('Code','Text')# header line
buffer = ['0', 'fake']    # give first pass through loop something to process
for line in input("GV_12.DXF"):
    line = line.rstrip()
    print(line)
    if line == '0':         # we've started a new section, so
        printpoint(buffer)      # handle the captured section
        buffer = []             # and start a new one
    buffer.append(line)

printpoint(buffer)        # buffer left over from last pass through loop
