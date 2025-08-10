try:
    num = int(input('Enter a num: '))
    print(f'Num: {num}')
except Exception as e:
    print(f'Exception Occured: {e}')
else:
    print('No Exception occurred')
finally:
    print('I Dont care..')