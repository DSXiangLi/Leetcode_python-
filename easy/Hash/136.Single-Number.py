"""
慢慢码系列 - Leetcode Python

136. Single number [Bit Operation] [Hash Table]

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

## hash table solution: O(N) time and need extra space
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] in hash_table:
                del hash_table[nums[i]]
            else:
                hash_table[nums[i]] = nums
        return list(hash_table)[0]

## bitwise operator: O(N) time and no need for extra space
# ^: bitwise exclustive, all numbers that shows 2 time leads to 0.
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1,len(nums)):
            result = result ^nums[i]

        return result

## Testing
def main():
    lines = input("Input number strings:")

    nums = [int(i) for i in lines]

    ret = Solution1().singleNumber(nums)
    print(ret)

    ret = Solution2().singleNumber(nums)
    print(ret)
