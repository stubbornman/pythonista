counter = dict()
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

for line in fh:
	if not line.startswith('From '):
		continue
	words = line.split()
	counter[words[1]] = counter.get(words[1],0) +1
#print counter
mostName = None
mostCount = None
for mail in counter:
   if mostCount == None or mostCount < counter[mail]:
      mostName = mail
      mostCount = counter[mail]
print mostName, mostCount       
    