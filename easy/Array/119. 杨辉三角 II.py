'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
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