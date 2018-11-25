"""
慢慢码系列 - Leetcode Python

219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = dict()
        for i in range(len(nums)):
            if (nums[i] in hash_table) and ((i - hash_table[nums[i]])<=k):
                return True
            else:
                hash_table[nums[i]] = i
        return False


def main():

    line = input("Input array here: ")

    k = int(input("Input K: "))

    nums = [int(i) for i in line.split(',')]

    result = Solution().containsNearbyDuplicate(nums, k)

    print("Whether array contain eligible pair", result)