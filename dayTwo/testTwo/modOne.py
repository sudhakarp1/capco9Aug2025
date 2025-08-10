dataOne = 100
dataTwo = 'Some string'
dataThree = [100, 200]

def funOne():
    print(f'funOne --> dataOne {dataOne} name: {__name__}')

def funTwo():
    print(f'funTwo --> dataTwo {dataTwo} name: {__name__}')

def funThree():
    print(f'funThree --> dataThree {dataOne} name: {__name__}')


if __name__ == '__main__':
    funOne()
    funTwo()
    funThree()