name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counter = dict()

for line in fh:
	if not line.startswith('From '):
		continue
	words = line.split()
#print words
	counter[words[1]] = counter.get(words[1],0) +1

lst = list()
for address,count in counter.items():
	lst.append((address,count))
	lst.sort(reverse=True)
	most = lst[0:1]
for email,count in most:
	print email, count
#print lst[0:1]