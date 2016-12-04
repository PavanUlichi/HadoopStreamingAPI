#!/usr/bin/python

import sys

for j, line in enumerate(sys.stdin, -1):
        if (j>=0):
                line = line.strip()
                words = line.split(",")
                count = 0
                length = len(words)
                for i in reversed(words):
                        if ( count < 5 and i != ""):
                                print '%s\t%s' % (i, 1)
                        count = count + 1
