#!/usr/bin/python

'''
https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/


A 3x3 magic square is a 3x3 grid of the numbers 1-9 such that each row, column, and major diagonal adds up to 15. Here's an example:
8 1 6
3 5 7
4 9 2
The major diagonals in this example are 8 + 5 + 2 and 6 + 5 + 4. (Magic squares have appeared here on r/dailyprogrammer before, in #65 [Difficult] in 2012.)
Write a function that, given a grid containing the numbers 1-9, determines whether it's a magic square. Use whatever format you want for the grid, such as a 2-dimensional array, or a 1-dimensional array of length 9, or a function that takes 9 arguments. You do not need to parse the grid from the program's input, but you can if you want to. You don't need to check that each of the 9 numbers appears in the grid: assume this to be true.


'''

import numpy


def list_to_grid(l, x, y):
  ''' given a list, L, with dimensons x and yreturns an matrix (list of lists)
  horizontally populated by the data in the list. '''
  matrix = []
  for hori in range(y):
    line = []
    for vert in range(x):
      item, l = l[0], l[1:]
      line.append(item)
    matrix.append(line)
  return matrix

# simple function test data.
testdata1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
testmatrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert list_to_grid(testdata1, 3, 3) == testmatrix1
testdata2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
testmatrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
assert list_to_grid(testdata2, 3, 4) == testmatrix2


def verticals(m):
  ''' given a matrix (list of lists), returns the flipped grid to turn the 
  horizonal list into vertical lists as a list of tuples.'''
  return zip(*m)

# simple function test data.
transposed1 = verticals(testmatrix1) 
assert transposed1 == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
transposed2 = verticals(testmatrix2)
assert transposed2 == [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]

def test_h(matrix, num):
  for line in matrix:
    if sum(line) != num:
      return False
    return True

# simple function test data
test1 = [8, 1, 6, 3, 5, 7, 4, 9, 2]
matrix1 = list_to_grid(test1, 3, 3)
assert test_h(matrix1, 15) == True

def test_v(matrix, num):
  matrix = verticals(matrix)
  for line in matrix:
    if sum(line) != num:
      return False
    return True

matrix2 = list_to_grid(test1, 3, 3)
assert test_v(matrix2, 15) == True

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


def test_d(matrix, num):
  diags = diagonals(matrix)
  majors = [diag for diag in diags if (len(diag) == len(matrix))] 
  for line in majors:
    if sum(line) != num:
      return False
    return True  

assert test_d(matrix2, 15) == True 


def test_square(magic_square):
  if test_h(magic_square, 15) and test_v(magic_square, 15) and test_d(magic_square, 15):
    return True
  else:
    return False


test1 = [8, 1, 6, 3, 5, 7, 4, 9, 2] # => true
test2 = [2, 7, 6, 9, 5, 1, 4, 3, 8] # => true
test3 = [3, 5, 7, 8, 1, 6, 4, 9, 2] # => false (h = true, v = false) 3,8,4 5,1,9 7,6,2
test4 = [8, 1, 6, 7, 5, 3, 4, 9, 2] # => false
matrix1 = list_to_grid(test1, 3, 3)
matrix2 = list_to_grid(test2, 3, 3)
matrix3 = list_to_grid(test3, 3, 3)
matrix4 = list_to_grid(test4, 3, 3)

assert test_square(matrix1) == True
assert test_square(matrix2) == True
assert test_square(matrix3) == False
assert test_square(matrix4) == False
