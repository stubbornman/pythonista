fhand = open('mbox.txt')
count = 0
for line in fhand:
    #line = line.rstrip('')
    if line.startswith('From:'):
        #count = count +1
    	print line, #count