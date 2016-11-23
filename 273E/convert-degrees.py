#!/usr/bin/python

'''
You will be given two lines of text as input. On the first line, you will receive a number followed by two letters, the first representing the unit that the number is currently in, the second representing the unit it needs to be converted to.
Examples of valid units are:
d for degrees of a circle
r for radians

radians = degrees * (pi/180)
degrees = radians * (180/pi)

'''

import math

input1 = '3.1416rd' # 180d
input2 = '90dr'     # 1.56r

def r2d(rads):
  return float(rads) * (180.0 / math.pi)

def d2r(degrees):
  return float(degrees) * (math.pi / 180.0)

def calculate(x):
  num, ops = x[:-2], x[-2:]
  if ops == 'rd':
    result = r2d(num)
    return str(result) + 'd'
  if ops == 'dr':
    result = d2r(num)
    return str(result) + 'r'
  else:
    print('I should not happen.')


print(calculate(input1))
print(calculate(input2))
