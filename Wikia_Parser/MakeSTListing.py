__author__ = 'tom'
import os

filename = "C:\\Users\\Tom\Desktop\OST.txt"

count = 1
with open(filename) as f:
    for line in f:
        result = '|-\n| style="text-align:center;" |%s\n|\n%s\n|' % (count, line.strip("\n"))
        print(result)
        count += 1