lst = list(range(1,10,2))
print(lst)
lst.append(100)
lstOne = lst[:] # shallow copy
lstOne.append(500)
print(lst)
print(lstOne)
