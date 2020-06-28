"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
