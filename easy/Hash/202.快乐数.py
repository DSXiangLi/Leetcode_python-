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
    def isHappy(self, n: int) -> bool:
        def calc(i):
            num = 0
            while i>0:
                i, mod = divmod(i,10)
                num+= mod**2
            return num

        reverse_set = set()
        while (n !=1) and (n not in reverse_set):
            reverse_set.add(n)
            n = calc(n)
        return n==1

def main():
    Input = input("Input the starting number here: ")
    Input = int(Input)

    result = Solution().isHappy(Input)

    print("{} is a Happy Number ? {}".format(Input, result))
