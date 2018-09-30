'''
26. Remove Duplicates from Sorted Array 
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index +=1
                nums[index] = nums[i]
        return index + 1 
            
			