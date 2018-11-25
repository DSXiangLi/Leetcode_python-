"""
慢慢码系列 - Leetcode Python

26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place
 such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2,
 with the first two elements of nums being 1 and 2 respectively.


"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int2
        """
        if not nums:
            return 0
        index = 0
        for i in range(1,len(nums)):
            or
            if nums[i] != nums[index]:
                index +=1
                nums[index] = nums[i]
        nums = nums[:index]
        return (index+1)

def main():
    input_string = input('Input your array here: ')
    array = [int(i)  for i in input_string.split(",")]
    print('Original array  is = {}'.format(array))
    unique_element = Solution().removeDuplicates(array)
    print('Remove duplicated array  is = {}'.format(array))
    print("unique element = {}".format(unique_element ))