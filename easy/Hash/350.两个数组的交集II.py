"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

#        return self.one_hash_table_solution(nums1, nums2)
        return self.two_hash_table_solution(nums1, nums2)
#       return self.sorted_array_solution(nums1, nums2)
#        return self.array_solution(nums1, nums2)

    def one_hash_table_solution(self,nums1,nums2):
        hash1 = dict()
        result = list()

        for i in range(len(nums1)):
            if(nums1[i] in hash1):
                hash1[nums1[i]] += 1
            else:
                hash1[nums1[i]] = 1

        for i in range(len(nums2)):
            if (nums2[i] in hash1) and (hash1[nums2[i]] >0):
                hash1[nums2[i]] -=1
                result.append(nums2[i])
        return result

    def two_hash_table_solution(self,nums1,nums2):
        hash1 = dict()
        hash2 = dict()
        result = list()

        for i in range(len(nums1)):
            if(nums1[i] in hash1):
                hash1[nums1[i]] += 1
            else:
                hash1[nums1[i]] = 1

        for i in range(len(nums2)):
            if(nums2[i] in hash2):
                hash2[nums2[i]] += 1
            else:
                hash2[nums2[i]] = 1

        for key in hash1.keys():
            if key in hash2:
                result += min(hash1[key], hash2[key]) * list(key)
        return result

    def sorted_array_solution(self, nums1, nums2):
        result = list()
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i=0;j=0;
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i]== nums2[j]:
                result.append(nums1[i])
                i +=1
                j +=1
            else:
                j +=1

        return result

    def array_solution(self, nums1, nums2):
        """
        Slowest solution. No extra stroage is needed
        Because 'in' and 'remove' operation both take O(N) time
        """
        result = list()

        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    result.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    result.append(i)
                    nums1.remove(i)
        return result


def main():
    nums1 = input("Input number 1: ")
    nums2 = input("Input number 2: ")

    nums1 = [int(i) for i in nums1.split(",")]
    nums2 = [int(i) for i in nums2.split(",")]

    result = Solution().intersect(nums1,nums2)

    print("Intersection is ",result)

