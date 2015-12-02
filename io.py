### I/O Methods
import csv

''' Extracting scientificnames to their own file, and putting them in memory '''
# Could do a cache, or have it spit out the good ones, and then smash those again API
def shortextrator(inputfile, *args): # fieldnames,
	names = []

	with open(inputfile, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			names.append(row['scientificname'])

	return names

def longextrator(inputfile, *args): # fieldnames,
	names = []
	testname = ""

	with open(inputfile, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			testname = [row['genus'], row['specificepithet'], row['infraspecificepithet']]
			testname = ' '.join(testname).split()
			names.append(' '.join(testname))

	return names

			# for field in fieldnames:
			# 	testname.append(row[field])
			# ' '.join(testname)

''' Writing out names to their own file '''
def depositor(outputfile, names, *args):
	with open(outputfile, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['scientificname'])
		writer.writeheader()
		for name in names:
			writer.writerow({'scientificname': name})