'''
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

# space O(n), time O(n)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        hash = dict()
        if length <= 2:
            return nums[0]
        
        for i in range(length):
            if nums[i] in hash:
                hash[nums[i]] += 1
                if hash[nums[i]] > length/2:
                    return nums[i]
            else:
                hash[nums[i]] = 1

# Time O(nlogn), space O(n)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	return sorted(nums)[int(len(nums)/2)] 
	
# tricky solution. Since the majority element > len/2. its count has bigger than everything else. 
# time O(n), SPace O(1)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        tmp = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                count = 1
                tmp = nums[i]
            else:
                if tmp == nums[i]:
                    count +=1
                else:
                    count -=1
        return tmp 
	