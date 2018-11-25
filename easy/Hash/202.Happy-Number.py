"""
慢慢码系列 - Leetcode Python

202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1 + 81 = 82
64 + 4 = 68
36 + 64 = 100
1 + 0 + 0 = 1

"""

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash_table = dict()
        hash_table[n] = 1
        while True:
            tmp = n
            n = 0
            while(tmp>=10):
                n += (tmp%10)**2
                tmp = tmp//10
            n += tmp**2
            if n==1:
                return True
            if n in hash_table:
                return False
            else:
                hash_table[n] = 1

def main():
    Input = input("Input the starting number here: ")
    Input = int(Input)

    result = Solution().isHappy(Input)

    print("{} is a Happy Number ? {}".format(Input, result))
