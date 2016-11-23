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

test1 = [8, 1, 6, 3, 5, 7, 4, 9, 2] # => true
test2 = [2, 7, 6, 9, 5, 1, 4, 3, 8] # => true
test3 = [3, 5, 7, 8, 1, 6, 4, 9, 2] # => false (h = true, v = false) 3,8,4 5,1,9 7,6,2
test4 = [8, 1, 6, 7, 5, 3, 4, 9, 2] # => false


def test_h(m):
  if m[0] + m[1] + m[2] == 15 and m[3] + m[4] + m[5] == 15 and m[6] + m[7] + m[8] == 15:
    return True
  else:
    return False

def test_v(m):
  if m[0] + m[3] + m[6] == 15 and m[1] + m[4] + m[7] == 15 and m[2] + m[5] + m[8] == 15:
    return True
  else:
    return False

def test_d(m):
  if m[0] + m[4] + m[8] == 15 and m[2] + m[4] + m[6] == 15:
    return True
  else:
    return False

def test_square(magic_square):
  if test_h(magic_square) and test_v(magic_square) and test_d(magic_square):
    return True
  else:
    return False


print test_square(test1)
print test_square(test2)
print test_square(test3)
print test_square(test4)
