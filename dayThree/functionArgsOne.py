def funOne(a, b):
    print(f'Positional args a: {a}  b: {b}')

def funTwo(a=10, b=20):
    print(f'Positional args default value a: {a}  b: {b}')

def funThree(a=1, b=2, *args):
    print(f'default and variable args a: {a} b: {b} args: {args}')

def funFour(a=1, b=2, *args, **kwargs):
    print(f'args and kwargs a: {a} b: {b} args: {args} kwargs: {kwargs}')

if __name__ =='__main__':
    funFour('a',b=100)

    #funFour(1,2,30,40, one=1, two=2)
    #funFour(one=1, two=2), 
    #funFour(1,2)
    #funFour(10,20,one=1, two=2)
    
    #funThree()    
    #funThree(10,20)
    #funThree(100,200, 30, 40, 50, 'a', 'b', 'c')

    #funTwo()
    #funTwo(1)
    #funTwo(1, 2)
    
    #funOne(10,20)
    #funOne('hello', 'world')
