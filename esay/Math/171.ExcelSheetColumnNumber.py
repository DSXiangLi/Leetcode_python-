'''
171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for char in s:
            # 可以想象成26进制
            result = result *26 + (ord(char) - ord('A') + 1)
            
        return result 