'''
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max0 = 0
        cur0 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur0 +=1
            else:
                max0 = max(max0, cur0)
                cur0 = 0
        max0 = max(max0, cur0)
        return max0