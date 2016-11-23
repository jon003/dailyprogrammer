#!/usr/bin/env python

'''

Take any string of words, with or without punctuation, and outpout a typoglycemia-compatible word:
-first and last letter remain unchanged.
-remainder of letters in each word should be randomly re-arranged.

'''
import random

def typo_word(word):
	''' Take a string s, and perform the typoglycemia translation on it. '''

	if len(word) <= 1:
		return word

	else:
		first, last = word[0], word[-1]
		print 'DEBUG: first, last are: %s, %s' % (first, last)
		plaintext = word[1:-1]
		print 'DEBUG: plaintext is: %s' % plaintext
		cryptex = list(plaintext)
		random.shuffle(cryptex)
		print 'DEBUG: cryptex is %s' % cryptex
		return first + ''.join(cryptex) + last

print typo_word('Something')
