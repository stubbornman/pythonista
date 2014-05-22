fname = raw_input('Enter a file name:')
try:
	filehandle = open(fname)
except:
	print fname, 'does not exist'
for line in filehandle:
	line = line.rstrip()
	line = line.upper()
	print line