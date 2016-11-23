#!/usr/bin/python
#
# Problem:
# A series of long binary numbers (example:)
# 0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100 
# ...must be converted to "Hello World"
#
# The ascii extended character set is 8 bits, 0 to 255.  
# Given this is 88 digits long, it'll give you 11 characters and that makes sense.
#
# algorithm:
#  split string into chunks of 8 digits.
#  convert each chunk of 8 binary digits to an integer.
#  convert each integer into a letter
#  append each letter to a string
#  when all done, print string.
#
# Sample inputs from the exercise.
line1='0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100'
line2='0111000001101100011001010110000101110011011001010010000001110100011000010110110001101011001000000111010001101111001000000110110101100101'
line3='011011000110100101100110011001010010000001110010011010010110011101101000011101000010000001101110011011110111011100100000011010010111001100100000011011000110111101101110011001010110110001111001'

# so I can switch around without dealing with argv and stuff while I work on the problem.
line=line1

# definitely 8 characters
# now to split the line up into chunks of 8 characters

# The number of binary digits that make up each encoded letter.  
# I fiddled with this until I was sure it was extended ascii set, not ascii. 
letter_length = 8

# zero out our encoded word array (integers) and our decoded words (strings)
coded_letter = ''
words = ''

# iterate from 0 down to the total length of the line, and slice it up by letters
for i in range(0, len(line), letter_length):
  # extract 8 digits representing a letter
  coded_letter = line[i:i+letter_length]
  decimal_letter = int(coded_letter,2)
  ascii_letter = chr(decimal_letter)
  words = '%s%s' % (words, ascii_letter)
 
print words
