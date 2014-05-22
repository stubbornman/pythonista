fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'The file cannot be opened:' , fname
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
        #count = count + 1
        line = line.rstrip()
        stripped = line.replace(' ','')
        #print stripped 
        intpos = stripped.find(':')
        score = stripped[intpos+1:]
        score = float(score)
        total = total + score
        count = count +1
        #print score, count
#print total,count
average = (total/count)
print 'Average spam confidence:', average
#print 'There were', count, 'subject lines in', fname