"""
慢慢码系列 - Leetcode Python

27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[index] = nums[i]
                index +=1
        nums = nums[:index]
        return index

def main():
    input_string = input('Input your array here: ')
    array = [int(i)  for i in input_string.split(",")]
    val = int(input("Input value to remove: "))
    print('Original array  is = {}'.format(array))
    length = Solution().removeElement(array,val )
    print("Length after removing element = {}".format(length))
    print('After Removing array  is = {}'.format(array))
