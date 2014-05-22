filename = raw_input('Enter log file name:')

try:
	filehand = open(filename)
except:
	print 'log file does not exist. please check your spelling, etc.'
for line in filehand:
	line = line.rstrip()
	if line.find('disconnect')== -1:
		continue
	print line
	