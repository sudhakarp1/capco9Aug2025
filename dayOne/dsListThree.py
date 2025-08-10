lst = list(range(1,10,2))
print(lst)
lst.append([10,20,30])
print(lst)
lstOne = lst.copy() #lst[:] #shallow copy
print(lstOne)
lstOne.append(500)

lst[5].append(40)
print('*' * 50)
print(lstOne)
print(lst)