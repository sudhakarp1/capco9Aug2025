
class TestClass:
    def __init__(self):
        self.dataOne = 100
        self.dataTwo = 'Some string'
        self.dataThree = [100, 200]

    def funOne(self):
        print(f'funOne --> dataOne {self.dataOne} name: {__name__}')
        

    def funTwo(self):
        print(f'funTwo --> dataTwo {self.dataTwo} name: {__name__}')

    def funThree(self):
        print(f'funThree --> dataThree {self.dataOne} name: {__name__}')

if __name__ == '__main__':
    obj = TestOne()
    obj.funOne()
    obj.funTwo()
    obj.funThree()