'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
		
		for num in nums:
			if num != 0:
				nums[index] = num
				index += 1
		for i in range(index, len(nums)):
			nums[i] = 0
		