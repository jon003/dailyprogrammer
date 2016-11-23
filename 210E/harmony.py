""" Integer Harmony 
	from: https://www.reddit.com/r/dailyprogrammer/comments/32goj8/20150413_challenge_210_easy_intharmonycom/ """

''' psuedocode 
convert num1 to binary
convert num2 to binary
compare each digit, match += 1 for each matching digit
turn match into a %, return it.
'''

num1 = 100
num2 = 42
compat = 1

def to_bin(number):
  number = bin(number)
  number = str(number)
  number = number.lstrip('0b')
  return number

def compare(bin1, bin2):
  pass

print to_bin(num1)
print to_bin(65535)

#print "Compatibility: %d" % (float(compat) / 8 * 100)
