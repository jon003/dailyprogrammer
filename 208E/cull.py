#!/usr/bin/python

'''
Input:  You will be given many unsigned integers.
Output:  Find the repeats and remove them. Then display the numbers again.
'''

from sys import argv

script, input_file = argv

file = open(input_file)

raw = file.readline()
numbers = raw.split(' ')

for digit in numbers:
  
#  print '%s' % digit