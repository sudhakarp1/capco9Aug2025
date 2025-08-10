words = {'one': 1, 'two':2,'three':3,'four':4, 'five':5, 
        'six':6, 'seven':7, 'eight':8,'nine':9,'ten':10,
        'eleven':11, 'twelve':12, 'thirteen':13, 
        'fourteen':14, 'fifteen':15, 'sixteen':16, 
        'seventeen':17, 'eighteen':18,'nineteen':19, 
        'twenty':20,'thirty':30, 'forty':40, 'fifty': 50, 
        'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90 ,
        'hundred':100, 'thousand':1000, 'lakhs':100000,'crore': 10000000}

string = 'fifty eight crore ninety five lakhs eighty seven thousand nine hundred and thirty five'

temp, num, sum = 0,0,0
for word in string.split():
    if word in words:
        num = words[word]
        if num < 100:
            temp+=num 
        else:
            sum += temp * num 
            temp = 0
sum += temp 
print(f'Output: {sum}')
