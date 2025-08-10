'''
    Writing a class to perform basic numerical ops
    isEven() --> boolean
    factorial() --> int (result)
    isPalindrome() --> boolean
'''

class NumOps:
    def __init__(self, num):        
        if type(num) == type(5):
            self.num = num #self.num is instance data
        else:
            self.num = 10

    def isEven(self):
        return self.num % 2 == 0
    
    def isPalindrome(self):
        revnum = int(str(self.num)[::-1])
        return revnum == self.num
    
    def factorial(self):
        res = 1
        for i in range(2, self.num + 1):
            res *= i
        return res

    def disp(self): #instance function / method
        print(f'Num: {self.num}')

if __name__ == '__main__':
    obj1 = NumOps('Store a string here') #allocating memory and assigning
    obj2 = NumOps(5)

    obj1.disp()
    obj2.disp()
    
    print(obj1.factorial())
    print(obj2.factorial())

    print(f'Even: {obj1.isEven()}')
    print(f'Even: {obj2.isEven()}')

    print(f'palindrome: {obj1.isPalindrome()}')
    print(f'Palindrome: {obj2.isPalindrome()}')
