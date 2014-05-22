##get the file name##
filename = raw_input('Enter log file name:')
##check for validity##
try:
	filehand = open(filename)
except:
	print 'log file does not exist. please check your spelling, etc.'
	exit()
##get email to find
emailaddy = raw_input('Enter email in question:')
linecount = 0
for line in filehand:
	line = line.rstrip()
	if line.find(emailaddy)== -1:
		continue
	print line
	linecount = linecount + 1
	#print linecount
if linecount < 1:
	print ' Email not found in log file.'

	