#!/usr/bin/python

'''
read file, set up list of families(members).
  to optimize the possibility of assignment, sort the list of families by number of members, descending.
defs for valid assignment checks
create empty results table.
make a copy of the list, so you can delete names as assigned.
start at first name, perform an assignment, then move on.
keep going until assigned.

'''


from sys import argv

def read_families():
	''' Read in family file, turn into a list of lists, then sort by length, descending, and return it. '''
	script, filename = argv
	f = open(filename)
	new_families = []
	for family in f:
		names = family.split()
		new_families.append(names)
	families_sorted = sorted(new_families,key=len, reverse=true)
	return families_sorted
	f.close()

def is_family(name1, name2, families):
	for family in families:
		if name1 in family and name2 in family:
			return True
	return False

# function test code
#print(is_family('Alex', 'Andrea', families))
#print(is_family('Sean', 'Andrea', families))

def pick_pair(families, master):
	'''
		Get first name from families lists, and delete it.
		Get a second name from families lists
		Check first and second to see in same family
			if not, delete second name as well
			if in same family, try again.
		return the new family list, with the two names deleted and the matchin first and second name
	'''	

def main():
	families = read_families()
	masterlist = families[:]		# clone list, don't just point to it, so we have a clear list to iterate over


if __name__ == "__main__":
	main()
