#!/usr/bin/python

""" https://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/

Take a number, and add up the square of each digit. You'll end up with another number. 
If you repeat this process over and over again, you'll see that one of two things happen:

For example, starting with the number 12:
12+22=5
52=25
22+52=29
22+92=85
82+52=89
82+92=145
From this point on, you'll join the cycle described above.

Inputs: 
base 'b'
starting number 'n'
"""


def cycle(number, base):
	""" Cycle the number by the listed base, return the result. """
	num = str(number)
	base = int(base)
	result = 0
	for char in num:
		digit = int(char)
		result += digit ** base
	return result

def sadcycle(number, base):
	""" Run the cycle and store it until you find the sad cycle for a given number and base.  When discovered, return the cycle. """
	sad = []
#	newsad = cycle(number, base)
#	sad.append(newsad)
	match = 0

	while not match:
		newsad = cycle(number, base)
		if newsad in sad:
			match = 1
			print 'Found %d in %r' % (newsad, sad)
		else:	
			sad.append(newsad)
			print "Adding: %d" % newsad
			number = newsad

	# before returning sad, I should trim the items in front of the first match, so that we only return the cycle
	# I could, but I'm too lazy.
	return sad


if __name__ == '__main__':
	n = raw_input('Enter Number: ')
	b = raw_input('Enter Base: ')
	print sadcycle(n, b)