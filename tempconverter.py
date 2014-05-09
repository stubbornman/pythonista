print 'BROTEMP: A Temperature Converter for BROS'

temp = raw_input("Enter a Temperature: ") 
convert = raw_input("Convert to (F)ahrenheit or (C)elcius? ")
ftemp = int(temp)
ctemp = int(temp)
#Function for Fahrenheit to Celcius

def f2c(temp):
	c = (5.0/9.0) * (ftemp-32)
	return c

#Function for Celcius to Fahrenheit
def c2f(ctemp):
	f = (9.0/5.0) * ctemp + 32
	return f

##testing 
if convert == 'C':
	newtemp = f2c(ftemp) 
	print temp ,'Fahrenheit =' , newtemp, 'Celcius BRO!'
	print 'Thanks for using BROTEMP!!1'
else :  
	newtemp = c2f(ctemp)
	print temp ,'Celcius =' , newtemp, 'Fahrenheit BRO!'
	print 'Thanks for using BROTEMP!!1'
 	
