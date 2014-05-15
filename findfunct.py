text ="X-DSPAM-Confidence:    0.8475"
intpos = text.find(':')
print intpos
#endpos = text.find('5',intpos)
#print endpos
#data = text[intpos:endpos + 1]
stripped = text.replace(' ','')
print stripped
anotherway = stripped.find(':')
anotherans = stripped[anotherway +1:]
print anotherans, type(anotherans)
data = text[intpos+1:]
print data
data = float(data)
print data, type(data)

