#!/usr/bin/env python3

import sys

inputs = '''123
44.234
0x123N
3.23e5
1293712938712938172938172391287319237192837329
.25'''

data = inputs.split('\n')

import re

floatRegex = re.compile(r'^(\d)?\.(\d)+$')
intRegex = re.compile(r'^(\d)+$')
expRegex = re.compile(r'^(\d)+\.(\d)+e(\d)+$')


for item in data:
	f_test = floatRegex.search(item)
	i_test = intRegex.search(item)
	e_test = expRegex.search(item)
	if f_test:
		print(item + ' (float)')
	elif i_test:
		if int(item) > sys.maxint:
			print(item + ' (bignum)')
		else:
			print(item + ' (integer)')
	elif e_test:
		print(item + ' (exponent)')		
	else:
		print(item + ' (string)')