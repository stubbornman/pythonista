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
regularpay = 40 * rateint
overtime = 	(overtimerate * overtimehours) 
#overtimepay = overtime + regularpay
#if hoursint <= 40 : 
#	print 'Pay:' ,pay
#else : 
#	print 'Pay:' ,overtimepay


def computepay(h,r):
	payroll = h * r
	return payroll
	
fulltime = computepay(hoursint,rateint)

def overtimecompute(rpay,otpay):
	value = rpay + otpay 
	return value
overtimegross = overtimecompute(regularpay,overtime)

if hoursint <= 40 : 
	print 'Pay: ' ,fulltime
else :
	print 'Pay: ' ,overtimegross