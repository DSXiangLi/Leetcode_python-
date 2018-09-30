'''
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

'''
duplicate/count like question can bes solved with has table
with value being key, and appearance being the value 
'''
## O(n) space, O(n) time 
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        hash = dict()
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]] = 1 
        return False;
		
##Create set from List O(n). So below solution looks concise but is inherently the same as above. 
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        return len(nums)!= len(set(nums))