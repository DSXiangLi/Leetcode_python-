"""
慢慢码系列 - Leetcode Python

349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""
class Solution:

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)

        result = nums1.intersection(nums2)

        return list(result)


def main():
    nums1 = input("Input number 1: ")
    nums2 = input("Input number 2: ")

    nums1 = [int(i) for i in nums1.split(",")]
    nums2 = [int(i) for i in nums2.split(",")]

    result = Solution().intersection(nums1,nums2)

    print("Intersection is ",result)

