'''
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = int((left + right)/2 )
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid -1 
                
        return left 
        