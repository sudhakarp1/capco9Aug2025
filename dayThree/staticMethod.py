class Sample:
    def funOne(self):
        print('instance method')

    @staticmethod
    def funTwo():
        print('Static method')

    @classmethod
    def funThree(cls):
        return cls()
    
if __name__ == '__main__':
    obj = Sample()
    print(obj.funOne)
    print(Sample.funTwo)
    print(Sample.funThree)

