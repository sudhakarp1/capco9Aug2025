from random import randint
lst = []
for _ in range(10):
    lst.append(randint(1, 100))
print(lst)

lstOne = [randint(1,100) for _ in range(10)] #list comprehension
print(lstOne)
print('*' * 50)
lst.sort(reverse=True) #inplace sorting
print(lst)
print('*' * 50)
lstTwo = sorted(lstOne,reverse=True)
print(lstOne)
print(lstTwo)
