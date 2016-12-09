#!/usr/bin/python

import sys

#for skipping data analysis on the first line
for j, line in enumerate(sys.stdin, -1):
        if (j>=0):
                #taking each line into a variable "line"
                line = line.strip()
                #taking all the words in the line separated by comma to variable line
                words = line.split(",")
                count = 0
                length = len(words)
                #we are considering the last 5 elements of the array
                for i in reversed(words):
                        if ( count < 5 and i != ""):
                                print '%s\t%s' % (i, 1)
                        count = count + 1
