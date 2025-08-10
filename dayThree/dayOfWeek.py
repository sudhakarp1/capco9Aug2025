class Calendar:
    def __init__(self, dd=10, mm=8, yyyy= 2025):
        self.dd, self.mm, self.yyyy = dd, mm, yyyy

    def __isValid(self):
        valid = True 
        if self.dd > self.maxDays() and self.dd < 1:
            valid = False 
        
        if self.mm <= 1 and self.mm > 12:
            valid = False

        return valid

    def printCalendar(self):
        week,days = self.dayOfWeek(True), self.maxDays()
        print('Su Mo Tu We Th Fr Sa')
        for _ in range(week):
            print(f'{" ":3}', end='')
        for i in range(1, days+1):
            print(f'{i:2} ', end='')
            if (week + i) % 7 == 0:
                print()
        print()

    def isLeap(self,yy=0):
        yy = yy if yy else self.yyyy
        return yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0
      
    def dayOfWeek(self, first=False):
        dd = 1 if first else self.dd
        mm, yy, ce = self.mm, self.yyyy % 100, self.yyyy // 100
        mm = mm - 2 if mm > 2 else mm + 10  
        yy = yy - 1 if mm > 10 else yy
        week =  int(dd + (2.6 * mm - 0.2) + yy + yy//4 + ce //4 - 2 * ce) % 7

        return week

    def maxDays(self):
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

        if self.mm == 2 and self.isLeap():
            return 29
        
        return days[self.mm - 1]
        

    def monthName(self):
        months=['January','February','March', 'April', 'May',
                'June','July','August','September', 'October', 
                'November', 'December']
        
        if self.__isValid():
            return months[self.mm - 1]
        return 'Invalid Month'


if __name__ == '__main__':
    obj = Calendar(10,8,2025)
    #obj.printCalendar()
    #print(f'Today: {obj.dayOfWeek()}')
    print(f'1996: {obj.isLeap(1996)}')
    print(f'1900: {obj.isLeap(1900)}')
    print(f'1600: {obj.isLeap(1600)}')