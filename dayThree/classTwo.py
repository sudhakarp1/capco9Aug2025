class NumOps:
    def __init__(self, num):        
        if type(num) == type(5):
            self.num = num #self.num is instance data
        else:
            self.num = 10

    
    def disp(self): #instance function / method
        print(f'Num: {self.num}')

if __name__ == '__main__':
    obj1 = NumOps('Store a string here') #allocating memory and assigning
    obj2 = NumOps(20)

    obj1.disp()#printing the data
    obj2.disp()