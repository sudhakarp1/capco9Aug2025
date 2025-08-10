lst = list(range(1,10,2))
print(lst)
print(*lst)
#--------------------------
for i in lst:
    print(i, end=' ')
#---------------------------
print()
lst.append(100)
lst.insert(0, 200)
print(lst)
lstOne = lst # reference (alias or another name) 
lstOne.append(500)
print(lst)