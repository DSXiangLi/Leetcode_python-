"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 注意和谐数组不一定是连续的，坑爹啊

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) +1

        res = 0
        for i in dic:
            if i+1 in dic:
                res = max(res, dic[i] + dic[i+1])

        return res
