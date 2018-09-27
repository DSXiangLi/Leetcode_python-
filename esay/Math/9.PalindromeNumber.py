'''
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

'''

'''
lazy solution. change to string and then iterate through the whole series.  
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x< 0:
            return False
        x = str(x)
        length = len(x)
        for i in range(int(length/2) ):
            if(x[i] != x[length - 1- i]):
                return False
            
        return True

'''
Even more lazy. Use buildin reverse function 
'''		
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x< 0:
            return False
        
        return str(x) == str(x)[::-1]

'''
No need to change int to string 
'''



