'''
167. Two Sum II - Input Array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
'''

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]]+1, i+1] ## this order is ensured by the sorted array 
            else:
                hash[numbers[i]] = i
        return [] 
	
	