num=101

for divisible in range(2, num):
    if num % divisible == 0:
        print(f'{num} is NOT a Prime')
        break 
else:
    print(f'{num} is Prime')