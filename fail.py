import sys

class MyDate(object):
    
    def __init__(num1, num2, num3):
        if not check_month(num2):
            print 'input month error'
            raise
        if not check_day(num2, num3):
            print 'input day error'
            raise
        self.year_num = num1
        self.month_num = num2
        self.day_num = num3
