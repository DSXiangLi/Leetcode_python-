'''
643. Maximum Average Subarray I
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
'''

## space O(1), Time O(n)
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cursum = sum(nums[:k])
        maxsum = cursum  
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxsum = max(maxsum, cursum)
        return maxsum/k