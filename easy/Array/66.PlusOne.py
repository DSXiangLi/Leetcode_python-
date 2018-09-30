'''
66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

'''
use string to transform the number to string 
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = digits[0]
        for i in range(1,len(digits)):
            number = number * 10 +  digits[i]

        number = number + 1
        
        return[ int(x) for x in str(number)]

'''
use string to construct number also 
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ''.join(str(i) for i in digits)
        number = int(number) + 1 
        
        return[ int(x) for x in str(number)]

		
