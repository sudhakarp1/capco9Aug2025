var = 10 #global variable 

def funOne(argOne):#parameter / argument 
    varOne = 1000 #local variable/data
    print(f'funOne var : {var} varOne: {varOne} argOne: {argOne}')

def funTwo(arg):
    global var
    var += 10
    print(f'funTwo var : {var} arg: {arg}')

funOne(100)
funTwo(200)
funOne(20)