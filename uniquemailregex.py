import re
counter = dict()
name = raw_input('Enter file name: ')
if len(name) < 1 : name = 'mboxshort.txt'
fh = open(name)
for line in fh:
	line.rstrip()
	x = re.findall('^From ([a-zA-Z]\S*@\S*[a-zA-Z])',line)
	if len(x) > 0:
		#print x
		counter[x[0]] = counter.get(x[0],0) +1
		
lst = list()
for (email,count) in counter.items():
	lst.append((count,email))
	lst.sort(reverse=True)
	#print lst
for (c,e) in lst:
	print e, c