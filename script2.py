# TODO: 
#	readfile = "path"
#	outputfile = "path"
#	raw_input("")
#	number of items wanted
import csv
names = []

# Extracting scientificnames to their own file
def extrator(inputfile, outputfile, *args):
	with open('names_for_marcial.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			names.append(row['scientificname'])

	with open('cleaned_names.csv', 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['scientificname'])
		writer.writeheader()
		for name in names:
			writer.writerow({'scientificname': name})

# Getting the names in memory:
#	names = names[:1024]
#	Standalone
#		with open('names_for_marcial.csv', 'rb') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		for name in xrange(0,1024):
#			names.append(reader.next()['scientificname'])

# have a logger list~ that adds notes to each [index]

def main():
	empty = []
	firstPass = {}
	incomplete = {}
	wrongFormat = {}

	# Maybe return a [], with type of error as second index
	for index in xrange(1,len(names)):
		test = names[index].split()
		if len(test) > 2:
			wrongFormat[index] = checkSpecialCharacters(names[index])
		elif len(test) == 1:
			incomplete[index] = names[index]
		elif len(test) == 0:
			empty.append(index)
		else:
			# To API/Synonyms
			# check for firstPass[1] synonyms
			firstPass[index] = test # names[index]

	# Need to keep a log of the changes im doing...

def checkSpecificChars(char, name):
	if char in name:
		name.split()
		name.remove(char)
		return ' '.join(name) # turn into list, with change
	return name

def checkSpecialCharacters(wrongName):
	temp = wrongName # a string..
	charlist = ['sp.', 'cf.', 'sp', 'cf', '?']

	if ('?', 'cp', 'sp') in temp:
		for index in xrange(1,len(charlist)):
			temp = checkSpecificChars(charlist(index), temp)

	return temp

# def regex for spaces, maybe?
# that flowchart was BS.... lol.

# Log File
def log(names):
	logText = ""

	logText += "Name: " + names[index] + ", at position " + str(index) + " has " + "AN" + " issue\n"

	# Output
	with open('log.txt', 'w') as logfile: logfile.write(logText)

if __name__ == '__main__':
	main()