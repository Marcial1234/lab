given [[0],[1]]

make a touple?

# this is gonna be fun

def extrator(inputfile, fieldnames, ):
	testname = []
	names = {}
	count = -1

	*normal pipeline*
	Do------*log*-----*log*---- etc
	the way i have it now is to merge all the logged dictionaries at the end...
	just 'log' the keys on the subdivided dictionaries, but +names

	with regex:
		catch odd charaters and spaces
	after with len(x):
		subdivide into: empty, incomplete, binomials, trinomials, or wrongFormat
	further check wrongFormat ones:


	with open(inputfile, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			for fields in fieldnames:
				for field in fields:
					
					testname[fields.find(field)].append(row[field])
			names[++count] = [' '.join(testname)]
				
	return names