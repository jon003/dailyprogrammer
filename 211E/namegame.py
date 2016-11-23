#!/usr/bin/python

""" Play the name game.  
	rules: http://www.reddit.com/r/dailyprogrammer/comments/338p28/20150420_challenge_211_easy_the_name_game/ """

"""
name name, bo fl_b[random B/f/m replacement]
Bonana fanna fo fl_f
Fee fy mo fl_m
name!
"""

from sys import argv

script, name = argv

if name[0] == 'b':
	fl_b = name[1:]
else:
	fl_b = 'b' + name[1:]

if name[0] == 'f':
	fl_f = name[1:]
else:
	fl_f = 'f' + name[1:]

if name[0] == 'm':
	fl_m = name[1:]
else:
	fl_m = 'm' + name[1:]

if name[0] in 'aeiou':
	fl_m = 'm' + name
	fl_b = 'b' + name
	fl_f = 'f' + name

print '%s, %s, bo %s,' % (name, name, fl_b)
print 'Bonana fanna fo %s,' % fl_f
print 'Fee fy mo %s,' % fl_m
print '%s!' % name