#!/usr/bin/env python3

''' Calculate the shannon entropy of a string.

https://www.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/

The Shannon entropy H of input sequence X is calculated as:
 -1 times the sum of the frequency of the symbol i times the log base 2 of the frequency:

'''

from math import log
from collections import Counterjjj

challenge = '''122333444455555666666777777788888888
563881467447538846567288767728553786
https://www.reddit.com/r/dailyprogrammer
int main(int argc, char *argv[])'''

inputs = challenge.split('\n')

def entropy(s):
	sum = 0
	for i in Counter(s).values():
		sum += 


for i in inputs:
	entropy(i)