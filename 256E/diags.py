#!/usr/bin/python

'''

The oblique function slices a matrix (2d array) into diagonals.
The de-oblique function takes diagonals of a matrix, and reassembles the original rectangular one.

'''

import numpy as np

matrix_out = '''0
1 6
2 7 12
3 8 13 18
4 9 14 19 24
5 10 15 20 25 30
11 16 21 26 31
17 22 27 32
23 28 33
29 34
35'''

matrix_in = '''0  1  2  3  4  5
 6  7  8  9 10 11
12 13 14 15 16 17
18 19 20 21 22 23
24 25 26 27 28 29
30 31 32 33 34 35'''

def load_matrix(source):
  return [row.split() for row in source.split('\n')]

matrix = np.array(load_matrix(matrix_in))

diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
print [n.tolist() for n in diags]



