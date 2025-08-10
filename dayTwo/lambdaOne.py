expr = lambda x: x * 2
print(expr(10))

def funOne(func):
    print('Before func call')
    func()
    print('After func call')
    print('*' * 50)

def funTwo():
    print('FunTwo() called')

funOne(funTwo)