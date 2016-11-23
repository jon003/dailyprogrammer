#!/usr/bin/python

import string

plain = string.ascii_lowercase
cipher = plain[::-1]

d = dict(zip(plain,cipher))

test = raw_input()
result = ''

for char in test:
	result = result + d.get(char, char)  

print result
