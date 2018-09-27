'''
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
'''

'''
All f(x) = c can be solved by newton.
x1 = x0 - f(x0)/f'(x0) for f(x) to converge to 0.
'''
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root = num
        while root*root >num:
            root = int(root/2 + num/(2*root))
        return root*root==num