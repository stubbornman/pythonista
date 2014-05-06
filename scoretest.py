x = raw_input('Enter a Score: ')
try :
	x = float(x)
except : 
	print 'Please enter a number...'
	quit()
if x > 1.0 :
	print ' Please enter a score between 1.0 and 0.1'
elif x >= 0.9 : 
	print 'A'
elif x>= 0.8 :
	print 'B'
elif x>= 0.7 :
	print 'C'
elif x>= 0.6 :
	print 'D'
elif x<0.6 :
	print 'F'
else :
	print 'You have entered an incorrect value.'
