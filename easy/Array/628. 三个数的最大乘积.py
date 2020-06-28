"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_pos1, max_pos2, max_pos3 = -inf, -inf, -inf
        min_neg1, min_neg2, min_neg3 = inf, inf, inf
        for i in nums:
            print( max_pos1, max_pos2, max_pos3,
                   min_neg1, min_neg2, min_neg3 )
            if i >= 0:
                if i >= max_pos1:
                    max_pos3, max_pos2, max_pos1 = max_pos2, max_pos1, i
                elif (i < max_pos1) and (i >= max_pos2):
                    max_pos3, max_pos2 = max_pos2, i
                elif (i < max_pos2) and (i >= max_pos3):
                    max_pos3 = i

            if i < 0:
                if i < min_neg3:
                    min_neg3, min_neg2, min_neg1 = i, min_neg3, min_neg2
                elif (i >= min_neg3) and (i < min_neg2):
                    min_neg2, min_neg1 = i, min_neg2
                elif (i >= min_neg2) and (i < min_neg1):
                    min_neg1 = i
                else:
                    pass

        available = [i for i in [max_pos1, max_pos2, max_pos3,
                                 min_neg1, min_neg2, min_neg3] if (i != -inf) and (i != inf)]

        from itertools import combinations
        result = max( [a * b * c for a, b, c in combinations( available, 3 )] )

        return result





