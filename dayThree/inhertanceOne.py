class Base:
    def __init__(self):
        print('Base constructor')

    def __str__(self):
        return f'Base class'
    
    def funOne(self):
        print('Base funOne()')

class Derived(Base):
    def __init__(self):
        super().__init__() # base class
        print('Derived Constructor') 

    
    def funOne(self):
        print('Derived funOne()')
        #return super().funOne()   


if __name__ == '__main__':
    obj = Derived()
    obj.funOne()