'''
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
'''

# use buildin function 
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_sorted = sorted(nums)
        Flag = [a==b for (a,b) in zip(nums,nums_sorted)]
        
        if all(Flag):
            return 0
        else:
            return  len(Flag) - Flag[::-1].index(False) - Flag.index(False) 