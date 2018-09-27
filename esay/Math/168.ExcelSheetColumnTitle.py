'''
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
'''

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title= ''
        ord_a = ord('A')
        while n :
            res = (n-1)%26
            title = chr(res + ord_a) + title
            n = int((n- 1)/26) ## dosen't matter n-1,n-2 . Here just want to shrink n by 26
        return title