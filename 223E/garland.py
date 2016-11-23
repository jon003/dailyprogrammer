#!/usr/bin/python


''' https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/ '''

''' Given a word like onion, count the garlands and print the number of garlands.
	For instance, onion has 2 sequence matches [on]i[on]
	[c]erami[c] -> 1, [alf[a]lfa] -> 4 (overlapping OK)
'''

def garland(word):
	max = 0
	for size in range(len(word)):
		if word[0:size] == word[-size:]:
			max = size
	return max

print garland('onion')
print garland('alfalfa')
print garland('ceramic')
print garland('truck')

