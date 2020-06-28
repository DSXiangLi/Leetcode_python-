"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
