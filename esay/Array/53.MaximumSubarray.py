'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''
similar to max profit 
'''

class Solution(object):
    def maxSubArray(self, nums):
        maxsum = nums[0]
        curmax = nums[0]
        for i in range(1,len(nums)):
        # as long as cursum is not negative, keep accumulating 
            curmax = max(curmax + nums[i], nums[i])
            maxsum = max(maxsum, curmax)
        return maxsum
		

## Tricky approach without extra space. Do the accumulation in place

class Solution(object):
    def maxSubArray(self, nums):
		for i in range(1,len(nums)):
			if nums[i-1] >0:
				nums[i] += nums[i-1]
		return max(nums)
