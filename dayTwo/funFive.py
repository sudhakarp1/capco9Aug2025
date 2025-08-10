var = 10 #global variable 

def funOne(argOne):#parameter / argument 
    varOne = 1000 #local variable/data
    return f'funOne var : {var} varOne: {varOne} argOne: {argOne}'

def funTwo(arg):
    global var
    var += 10
    return f'funTwo var : {var} arg: {arg}'

res = funOne(100)
print(res)

print(funTwo(200))
print(f' calling funOne(20) here {funOne(20)}')
print(funOne('Hello'))

print(funOne(10) + funTwo('Some string'))