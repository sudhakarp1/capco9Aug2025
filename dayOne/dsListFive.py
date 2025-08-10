lst = list(range(1,10,2))
print(f'{lst} at {id(lst)}')
lst.extend([10,20,30])
lstOne = lst[:] #lst.copy() 
print(f'lst: {lst} at {id(lst)}')
print(f'lstOne: {lstOne} at {id(lstOne)}')

if lst == lstOne:
    print('Same')
else:
    print('Not Same')

lst.pop() #pops last element from lst

if lst < lstOne:
    print('lst less than lstOne')
else:
    print('lst NOT less than lstOne')

        