count = 0
total = 0
while True:
    userinput = raw_input('Enter a number: ')
    if userinput == 'done':
        break
    try:
        number = float(userinput)
    except:
        print 'Please use numbers only..'
        continue
    count = count + 1
    total = total + number
    average = total / count 
    
print total, count, average

    