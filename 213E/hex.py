#coding=utf-8
""" https://www.reddit.com/r/dailyprogrammer/comments/34rxkc/20150504_challenge_213_easy_pronouncing_hex/  """

def transbyte(input):
	bytes = {
		"a" : 'atta',
		"b" : 'bibbity',
		"c" : 'city',
		"d" : 'dickety',
		"e" : 'ebbity',
		"f" : 'fleventy'
	}
	nums = {
		'0' : '-bitey',
		'1' : 'one',
		'2' : 'two',
		'3' : 'three',
		'4' : 'four',
		'5' : 'five',
		'6' : 'six',
		'7' : 'seven',
		'8' : 'eight',
		'9' : 'nine',
		'a' : 'ayy',
		'b' : 'bee',
		'c' : 'cee',
		'd' : 'dee',
		'e' : 'eee',
		'f' : 'fee'
	}

	input = str(hex(input)[2:]).lower()

	if len(input) == 4:
		print input
		first = input[0]
		second = input[1]
		third = input[2]
		fourth = input[3]
		return bytes[first] + nums[second] + ' bitey ' + bytes[third] + '-' + nums[fourth]
	if len(input) == 2:
		first = input[0]
		second = input[1]
		return bytes[first] + '-' + nums[second]
	else:
		return 'Not a Hex Number'

#result = transbyte(0xF5)
#print result
print 'bibbity-three:  %s ' % transbyte(0xB3)
print 'ebbity-four:  %s' % transbyte(0xE4)
print 'bibbity-bee bitey bibbity-bee:  %s' % transbyte(0xBBBB)
print 'atta-bitey city-nine:  %s' % transbyte(0xA0C9)