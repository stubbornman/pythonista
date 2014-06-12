name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counter = dict()

for line in fh:
	if not line.startswith('From '):
		continue
	words = line.split()
	hour = words[5].split(':')
	#print type(hour)
	counter[hour[0]] = counter.get(hour[0],0) +1

lst = list()
for key,val in counter.items():
	lst.append((key,val))
lst.sort()
for key,val in lst:
	print key, val
	
#print lst
#print type(counter)
