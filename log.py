### Logs
logger = {}

def log(group, message, *args):
	for name in group:
		try: logger[name] += " and " + message # this wont happen much now, really
		except: logger[name] = message

def writeLog(logfile, names):
	logText = ""
	for index in sorted(logger):
		logText += names[index] + " (#" + str(index+1) + ") has: " + logger[index]

	with open('log.txt', 'w') as logfile: logfile.write(logText)
	
	# Needs to be a CSV
	# with open(outputfile, 'wb') as csvfile:
	# writer = csv.DictWriter(csvfile, fieldnames=['scientificname'])
	# writer.writeheader()
	# for name in names:
	# 	writer.writerow({'scientificname': name})