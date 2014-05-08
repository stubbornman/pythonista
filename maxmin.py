largest = None
smallest = None
while True:
    userinput = raw_input('Enter a number: ')
    if userinput == 'done':
        break
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
    elif smallest < number:
        continue
print 'Maximum is' , largest
print 'Minimum is' , smallest