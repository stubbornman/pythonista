#Function Fahrenheit to Celcius
def f2c(ftemp):
	c = (5.0/9.0) * (ftemp-32)
	return c

#Function for Celcius to Fahrenheit
def c2f(ctemp):
	f = (9.0/5.0) * ctemp + 32
	return f

####################################################
print 'BROTEMP: A Temperature Converter for BROS'
while True:

	temp = raw_input("Enter a Temperature: ") 
	try:
		ftemp = int(temp)
		ctemp = int(temp)
	except: 
		print 'Invalid Input, please use numbers only BRO.'
		continue
	convert = raw_input("Convert to (F)ahrenheit or (C)elcius? ")

	if convert == 'C':
		newtemp = f2c(ftemp) 
		print temp ,'Fahrenheit =' , newtemp, 'Celcius BRO!'
		again = raw_input('Go again? Y/N: ')
 		if again == 'Y':
 			continue
 		else:
 			break
	else :  
		newtemp = c2f(ctemp)
		print temp ,'Celcius =' , newtemp, 'Fahrenheit BRO!'
		
 		again = raw_input('Go again? Y/N: ')
 		if again == 'Y':
 			continue
 		else :
 			break
 		
print 'Thanks for using BROTEMP!!1'