#!/usr/bin/python
""" Converts dates from a variety of input formats and outputs dates in ISO 8601 """

import sys

script, input_file = sys.argv

def monthword_to_decimal(month):
	""" Takes Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec: Returns: 1-12 """
	months = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
			  'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'
			 }
	return months[month]


def two_to_four_digit_year(yearyear):
	""" Takes a two digit year, returns a 4 digit year in the range: 1950-2049 """
	if int(yearyear) < 49:
		return '20%s' % yearyear
	else:
		return '19%s' % yearyear

with open(input_file) as f:
    for line in f:
    	line = line.rstrip('\n')
        # syntax yyyy-mm-dd
        if '-' in line:
        	print line
		# syntax mm/dd/yy
        elif '/' in line:
        	(month, day, year) = line.split('/')
        	year = two_to_four_digit_year(year)
        	print "%s-%s-%s" % (year, month, day)
		# syntax mm#yy#dd
        elif '#' in line:
        	(month, year, day) = line.split('#')
        	year = two_to_four_digit_year(year)
        	print "%s-%s-%s" % (year, month, day)
		# syntax dd*mm*yyyy
        elif '*' in line:
        	(day, month, year) = line.split('*')
        	print "%s-%s-%s" % (year, month, day)
		# syntax month word) dd, yy
		# syntax (month word) dd, yyyy
        elif ',' in line:
        	(month, day, year) = line.split(' ')
        	day = day.rstrip(',')
        	month = monthword_to_decimal(month)
        	if int(year) < 100:
	        	year = two_to_four_digit_year(year)
        	print "%s-%s-%s" % (year, month, day)
        # throw an error if none of the regex match (unknown format)
        else:
        	print "ERROR: Could not decode: %s" % line
