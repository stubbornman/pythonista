#Set needed variables and gather inputs
largest = None
smallest = None
while True:
    userinput = raw_input('Enter a number: ')
    if userinput == 'done':
        break
    #Check to make sure it is a number that was entered
    try:
        number = int(userinput)
    except:
        print 'Invalid input'
        continue
    #Do the work here
    if largest is None:
        largest = number
    elif number > largest:
        largest = number
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
print 'Maximum is' , largest
print 'Minimum is' , smallest