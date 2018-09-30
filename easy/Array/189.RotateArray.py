'''
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

## list slicing O(n) space. temporary hold for the slice. O(n) time
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
		
## use list as stack O(1)space O(n) time. pop take O(1) time, insert take O(n) time 
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            val = nums.pop()
            nums.insert(0,val)