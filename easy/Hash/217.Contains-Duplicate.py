"""
慢慢码系列 - Leetcode Python

217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# use hash table O(N)
class Solution1:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return True
            else:
                hash_table[nums[i]] =1
        return False

# use set: faster with build in set function.
class Solution2:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        else:
            return True

def main():

    line = input("Input array :")

    nums = [int(i) for i in line.split(',')]

    result = Solution2().containsDuplicate(nums)

    print("The array contains duplicates: ",result)
