import random 
count = 0
numb = random.randrange(1,100)

#for testing - Uncomment below
#print numb 

print 'Time to play a guessing game. '
print("\n")
guess = raw_input('Enter a number between 1 and 100: ')
	
while True:
	try:
		guess = int(guess)
	except:
		guess = raw_input('Please use numbers only. No letters or symbols please. Try again: ')
		continue
	count = count + 1 
	if guess == numb:
		print 'Congratulations! You guessed correctly in',count, 'guesses!'
		break
	elif guess > numb:
		guess = raw_input('Too high. Try again: ')
		continue
	elif guess < numb:
		guess = raw_input('Too low. Try again: ')
		continue
	
	
		
