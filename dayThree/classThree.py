'''
    without constructor (__init__())
'''
class NumOps:
    def setNum(self, num):
        self.num = num #assign value 

    def disp(self): #print the value         
        print(f'Num: {self.num}')


if __name__ == '__main__':
    obj1 = NumOps() #allocating memory for storing data
    obj2 = NumOps()
    
    obj1.setNum('hello world is always used to start off any programming language') # storing the data
    obj2.setNum(20)

    obj1.disp()#printing the data
    obj2.disp()