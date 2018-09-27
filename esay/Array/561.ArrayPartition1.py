'''
561. Array Partition I 
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
'''


'''
min(a,b): half of the element need to have bigger values
best case is taking  1,3,5,7
'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        order_nums = sorted(nums)
        
        return(sum(order_nums[::2]))