try:
	hours = raw_input("Enter Hours: ") 
	hoursint = float(hours) 
	rate = raw_input("Enter Rate per Hour:")
	rateint = float(rate)
except:
	print 'Error: Please use numbers.'
	quit()
overtimehours = (hoursint - 40)
overtimerate = (rateint * 1.5)
pay = hoursint * rateint
overtimepay = 	(overtimerate * overtimehours) + (40 * rateint)
if hoursint <= 40 : 
	print 'Pay:' ,pay
else : 
	print 'Pay:' ,overtimepay
	