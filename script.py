#! /usr/bin/python

# TODO: 
#	number of items wanted
#	def regex for spaces, maybe?

# import json #, time #, os, math, numpy, pandas, etc...
import log as o, io, time, re

start = time.time()
# names = [] # needs a CACHE or DB
empty = {}
empty2 = {}
tbdeleted = []
binomials = {}
trinomials = {}
incomplete = {}
wrongFormat = {}

	
''' Working on some stuff to do => empty = (empty | empty2)
			# reverse the fieldnames.... Zzzz
			testname = [row['genus'], row['specificepithet'], row['infraspecificepithet']]
 			testname = ' '.join(testname)
 			temp = testname.split()
 			if temp == "":
				testname = row['scientificname']
				empty2[len(names)] = temp

			names.append(testname)
		# Do a testarr and return the array?
		# nuuu you're too big already D:
'''

# TBA
# def rangedExtrator(inputfile, end=len(names), *args): # inputfile
# 	with open(inputfile, 'rb') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		testname = []
# 		for row in reader:
# 			for x in xrange(0, hardEnd):
# 				for field in fieldnames:
# 					testname.append(row[fieldnames])
# 	 			testname = ' '.join(testname)
# 				names.append(testname)

# 97479 => ^oink.... | and & of this. wow... EP right here

### Cleaners
# Accepted documentation method/style?
''' 
	Accepts a string. Checks if specific characters are found separated by spaces

	TODO: Regex, check for odd spaces
'''
def checkSpecialCharacters(wrongName):
	tempName = wrongName.split()
	# '?' at the end, need regex..
	# " at the front
	# shorten middle 's.' & '(authors.)'
	charlist = ['sp.', 'cf.', 'sp', 'cf', '?', '(?)' # subdivision, DP?
	, 'ssp.', 'subsp.', '[illeg.]', '[illeg.]', '[illeg].'
	]
	# Do sevaral passes?

	for char in charlist:
		while True:
			if char in tempName:
				tempName.remove(char)
			else: break

	tempName = ' '.join(tempName)
	# REGEX HERE, do a loop and log each case.
	tempName = re.sub('[\"]', '', tempName)
	# does this work??? 
	# Why have it on the first place??

	return tempName.split() #' '.join(tempName)

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

##### MAIN! #####
def main():
	# inputfile = raw_input('Please enter the input file name: ') + '.csv' # 'names_for_marcial.csv'
	# shorterfile = raw_input('Please enter the output file name: ') + '.csv' # 'cleaned_names.csv'
	logfile = 'log.txt'
	inputfile = 'names_for_marcial.csv'
	shorterfile = 'cleaned_names.csv'
	fields = [['genus'],['specificepithet'],['infraspecificepithet']]


	''' Had some timing done, not really needed after access to school machines?? '''
	# io.extrator(inputfile, ['scientificname'])
	# names = io.shortextrator(inputfile)
	# print time.time() - start # 6.5 => CACHE!
	# print time.time() - start # 2.3
	names = io.extrator(inputfile)
	io.depositor(shorterfile, names)
	longnames = io.extrator(inputfile, fields, names)
	# Maps: #key : 'words'

	# Separate based on # of words
	# Needs own method?
	# this alone has all incompletes

	# Search for spaces before doing this..

	for key in names:
		# [/w/s+] => log as too many spaces

		test = len(names[key][0].split())
		if test >= 2:
			wrongFormat[index] = names[index]
		elif test == 1:
			incomplete[index] = names[index]
		elif test == 0:
			empty[index] = names[index]

	for item in wrongFormat:
		# Check for specific chars and delete them, 
		# return a list and repeat as above
			# need to pass a charlist eventually
		test = len(checkSpecialCharacters(wrongFormat[item]))
		# test2 = len(checkSpecialCharacters(longnames[item]))

		if test < 4:
			tbdeleted.append(item)
			if test == 2:
				binomials[item] = wrongFormat[item]
			elif test == 3:
				trinomials[item] = wrongFormat[item]
			elif test == 1:
				incomplete[item] = names[item]
			elif test == 0:
				empty[item] = names[item]

	# print time.time() - start # 2.4

	# Clean the newly fixed ones
	for key in tbdeleted:
		del wrongFormat[key]

	# turn it into a ng-repeat? :D
	o.log(empty, "Specific wrong interpretation of Darwin Core\n")
	o.log(incomplete, "Cannot be processed further since it only has one word (Genus or Superclass)\n")
	# Would need to get the genus and spefic epiteh

	# Union:
	# list(set(a) | set(b))
	# Intersection:
	# list(set(a) & set(b))
	# Run 'main' twice, do above, log and $$
	# Nope, ^ is better

	# All maps
	print len(empty) # 10391
	print len(incomplete) # 33675
	print len(wrongFormat) # 58334
	print len(binomials) # 219473
	print len(trinomials) # 115337
	# output this to files for the time being

	# SHOW FIRST FEW
	# for index in xrange(0,2000):
	# 	try:
	# 		print binomials[index]
	# 	except Exception, e:
	# 		pass
	# 	try:
	# 		print trinomials[index]
	# 	except Exception, e:
	# 		pass

	# ALL ODD ONES
	# 3518 '.' , 2609 '?' , 3212 '(' , 3575 ')' , 304 '[' , 329 ']' , 5 '{' , 5 '}'
	# 
	# count1 = 0
	# count2 = 0
	# for item in binomials:
	# 	if '}' in binomials[item]:
	# 		count1 += 1
	# for item in trinomials:
	# 	if '}' in trinomials[item]:
	# 		count2 += 1
	# print ""
	# print count1 + count2
	# Ready for synonyms check


	# No bueno...
	names2 = merge_dicts(empty, incomplete, wrongFormat, binomials, trinomials)
	o.writeLog(logfile, names2)
	print time.time() - start

if __name__ == '__main__':
	main()