'''
118. Pascal's triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''

## Tricky solution
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1,numRows):
            pascal.append( [sum(pair) for pair in zip(pascal[-1]+[0], [0] + pascal[-1])] ) 
                          
        return pascal