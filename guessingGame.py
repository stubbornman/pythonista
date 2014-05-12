import random 
count = 0
numb = random.randrange(1,100)
#Loop to Generate random number between 1-100 and save it.
print numb 

while True:

	guess = raw_input('Enter a number between 1 and 100: ')
	try:
		guess = int(guess)
	except:
		print 'Please use the number keys, no letters.'
	count = count + 1 
	if guess == numb:
		print 'Congratulations! You guessed correctly in',count, 'guesses!'
		break
	elif guess > numb:
		print 'Too high. Try again.'
		continue
	elif guess < numb:
		print 'Too low. Try again.'
		continue
	else:
		break
		
