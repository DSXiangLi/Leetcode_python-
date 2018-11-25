"""
慢慢码系列 - Leetcode Python

350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
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

