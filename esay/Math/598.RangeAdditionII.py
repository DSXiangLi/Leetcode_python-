'''
598. Range Addition II
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.
'''

'''
much concise solution 
'''
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) ==0:
            return m*n
        
        return min(op[0] for op in ops) * min(op[1] for op in ops )

'''
verbose....solution 
'''
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) ==0:
            return m*n
        m = ops[0][0]
        n = ops[0][1]
        for tmp in ops[1:]:
            m = min(m, tmp[0])
            n = min(n, tmp[1])
        
        return m*n
        