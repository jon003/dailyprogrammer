#!/usr/bin/env python3



listdata =	[[-2,  5,  3,  2],
        	[ 9, -6,  5,  1],
        	[ 3,  2,  7,  3],
        	[-1,  8, -4,  8]]


import numpy

def diagonals(listdata):
	''' Takes a list of equal length lists representing a grid or matrix, 
	and returns all of the diagonal columns, in both a 'forward leaning' 
	and 'reverse leaning' manner. 
	
	Credit to:
	http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
	'''
	
	a = numpy.array(listdata)

	diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

	diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

	return [n.tolist() for n in diags]


results = diagonals(listdata)
print(results)



