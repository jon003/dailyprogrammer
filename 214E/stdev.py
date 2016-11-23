#!/usr/bin/python
""" http://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/ 

1. Calculate mean (sum of all divided by number of entries in the population)
2. For each value in the population calculate the difference between it and the mean value, and square that difference.
3. Calculate the sum of all the values from the previous step.
4. Divide that sum by the number of values in the population.  The result is known as the variance of the population.
5. Finally, to get the standard deviation, take the square root of the variance.

"""

from math import sqrt
from numpy import std

a = [5,6,11,13,19,20,25,26,28,37] 								# 9.7775
b = [37,81,86,91,97,108,109,112,112,114,115,117,121,123,141] 	# 23.2908
#c = [266 344 375 399 409 433 436 440 449 476 502 504 530 584 587]
#d = [809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373] 

def standard_deviation(population):
	""" Return the standard deviation of a population (list) of values """
	mean = float(sum(a)) / len(a)
	x = float(0)
	for value in population:
		difference = abs(value-mean)
		squarediff = difference ** 2
		x += squarediff
	variance = x / len(a)
	return sqrt(variance)

print 'Result: %0.4f, Should be: %0.4f' % (standard_deviation(a), std(a))
print 'Result: %0.4f, Should be: %0.4f' % (standard_deviation(b), std(b))
