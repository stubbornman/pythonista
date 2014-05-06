try:
	enternumb = raw_input("Enter a Number: ") 
	numbint = float(enternumb) 
except:
	print 'Invalid input.'
		
total = 0 
for itervar in [numbint]:
	total = total + itervar
print 'Total:' , total		
