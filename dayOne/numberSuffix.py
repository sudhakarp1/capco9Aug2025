var = int(input('Input a number: '))
#1023
print(f'Suffix: {var}', end="")
if var % 10 == 1 and var % 100 != 11:
    print('st')
elif var % 10 == 2 and var % 100 != 12:
    print('nd')
elif var % 10 == 3 and var % 100 != 13:
    print('rd')
else:
    print('th')
