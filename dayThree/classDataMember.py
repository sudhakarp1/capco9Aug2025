class Sample:
    classData = 'Sample class Example'

    def funOne(self):
        print(f'funOne() class Data: {self.classData}')
    
    def funTwo(self):
        print(f'funTwo() class Data: {self.classData}')

if __name__ == '__main__':
    print(f'data: {Sample.classData}')

    obj = Sample()
    obj.funOne()
    
    obj2 = Sample()
    obj2.funTwo()
    obj2.classData = 'No more data'#shadowing
    obj2.funTwo()
    obj2.funOne()

    obj.funOne()
    obj.funTwo()