text ="X-DSPAM-Confidence:    0.8475"
intpos = text.find('0')
print intpos
endpos = text.find('5',intpos)
print endpos
data = text[intpos:endpos + 1]
data = float(data)
print data 

