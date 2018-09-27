'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''

'''
I prefer newton method. 
f(x') = x- x'^2 = 0 =  f(x0) - 2(x'-x0)*x0 = 0 
x' = x/2x0 + x0/2
You can also solve with Binary Search
'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x0 = x
    
        while x0**2 > x:
            x0 = x/(2*x0) + x0/2
            x0 = int(x0)

        return x0