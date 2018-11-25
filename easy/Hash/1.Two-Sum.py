"""
慢慢码系列 - Leetcode Python

1. Two Sum [Hash Table]

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()
        hash_table[nums[0]] = 0

        for i in range(1,len(nums)):
            if (target - nums[i]) in hash_table:
                return [hash_table[target - nums[i]], i]
            else:
                # because there is only one solution. no duplicates needed
                hash_table[nums[i]] = i

def main():

    lines = input("Input number strings:")

    nums = [int(i) for i in lines.split(' ') if len(i)>0]

    print(nums)

    target = int(input("Input target:"))

    result = Solution().twoSum(nums, target)

    print(result)
