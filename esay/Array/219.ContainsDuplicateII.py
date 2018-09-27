'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

'''

'''
Duplicate problem can be solved either by hash or by set. generally depends on what information needed to be returned.z
'''

def containNearbyDuplicate(self, nums, k ):
	hash = dict()
	if not nums:
		return False
	for i in range(len(nums)):
		if nums[i] in hashn and i - hash[nums[i]] <=k:
			return True
		else:
			hash[nums[i]] = i ## replace with a bigger index 
	return False 