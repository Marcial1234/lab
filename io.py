### I/O Methods
import csv


# Combine into ONE SUPREME METHOD!

''' Extracting scientificnames to their own file, and putting them in memory '''
# Could do a cache, or have it spit out the good ones, and then smash those against the API
def extrator(inputfile, ): # fieldnames,
	count = -1
	names = {}

	with open(inputfile, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			count += 1
			names[count] = row['scientificname']

	return names

''' Takes a list of fields to be merged and checed against existing names '''
''' Doesn't delete spaces by default '''
# If name !good: xor+=name
def extrator(inputfile, fieldnames, names): # fieldnames,
	count = -1
	newnames = {}
	testname = []

	with open(inputfile, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			for fields in fieldnames:
				testname.append(row[field])
			testname = ' '.join(testname)
			count += 1
			if names[count] != testname:
				newnames[count] = testname

	return newnames

''' Writing out names to their own file '''
def depositor(outputfile, names, ):
	with open(outputfile, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['scientificname'])
		writer.writeheader()
		for name in names:
			writer.writerow({'scientificname': name})


# TBA
# def rangedExtrator(inputfile, end=len(names), *args):
# 	with open(inputfile, 'rb') as csvfile:
# 	reader = csv.DictReader(csvfile)
# 	testname = []
# 	for row in reader:
# 		for x in xrange(0, hardEnd):
# 			for field in fieldnames:
# 				testname.append(row[fieldnames])
# 				testname = ' '.join(testname)
# 			names.append(testname)