expr = lambda x: x * 2

def funOne(func, arg):
    print(f'Before func call {func.__name__}')
    func(arg)
    print('After func call')
    print('*' * 50)

def funTwo(arg):
    print(f'FunTwo({arg}) called')

funOne(funTwo, 1000)
funOne(expr, 100)
funOne(lambda x: x * x, 10)