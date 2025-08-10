def getInput():
    string = ''
    while True:
        try:
            string = input('Enter a value')

            if 'Stop' not in string :
                raise TypeError('Include stop in your input')
        except TypeError:
            continue
        else:
            break
    return string 

strIn = getInput()
print(f'Got: {strIn}')    
    
