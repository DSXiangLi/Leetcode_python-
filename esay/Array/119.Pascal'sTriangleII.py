'''
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
'''

#flow the previous method,  Time O(n^2), space()
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tmp = [1]
        if rowIndex == 0:
            return tmp 
        
        for i in range(rowIndex):
            tmp = [sum(pair) for pair in zip(tmp + [0], [0] + tmp)]

        return tmp