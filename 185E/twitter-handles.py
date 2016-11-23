#!/usr/bin/python
""" https://www.reddit.com/r/dailyprogrammer/comments/2jt4cx/10202014_challenge_185_easy_generated_twitter/ """

short_handles = []

with open ('enable1.txt') as f:
	for word in f:
		word = word.strip()
		if 'at' in word:
			handle = word.replace('at', '@')
			if len(handle) <= 10:
				short_handles.append(handle)

sorted_handles = sorted(short_handles, key=len)

for handle in sorted_handles:
	print handle