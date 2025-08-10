def getInput():
    string = ''    
    try:
        string = input('Enter a value')

        if 'Stop' not in string :
            raise TypeError('Include stop in your input')
    except TypeError:
       string = getInput()
    
    return string 

strIn = getInput()
print(f'Got: {strIn}')    
    
