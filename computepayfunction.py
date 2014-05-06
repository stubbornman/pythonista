def computepay(hours,rate):
	if hours <= 40 :
		pay = (hours * rate)
		return pay
	else  :
		pay = (rate * 40) + (rate * 1.5 * (hours - 40))
		return pay

try:
	hours = raw_input("Enter Hours: ") 
	hours = float(hours) 
	rate = raw_input("Enter Rate per Hour:")
	rate = float(rate)
except:
	print 'Error: Please use numbers.'
	quit()

pay = computepay(hours,rate) 
print   pay