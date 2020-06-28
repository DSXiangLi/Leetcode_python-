"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
通过次数14,986提交次数38,750

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum = sum(nums[:k])
        maxsum = cursum
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxsum = max(cursum, maxsum)
        return maxsum/k