'''
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''

'''
Tricky solution
num = 100a + 10b +c --> a+b+c
Because 100%9=1 & 10%9=1 
num%9 == (a+b+c)%9
Keep doing this until 1 digits is left 
'''
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <10:
            return num
        if num%9 ==0:
            return 9
        else:
            return num%9