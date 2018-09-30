'''
532. K-diff Pairs in an Array
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
'''

'''
Time O(n) iterate through the entire list 1 time 
unique pairs are ensured by whether current key in the hash 
'''
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = dict()
        ## unique number pair, not unique index pair
        if k <0: 
            return 0 
        for i in range(len(nums)):
            if nums[i] not in hash and k!=0:
                hash[nums[i]] = 0
                if nums[i] - k in hash:
                    hash[nums[i]-k] +=1
                if nums[i] + k in hash:
                    hash[nums[i]+k] +=1 
            elif nums[i] in hash and k==0:
                hash[nums[i]] = 1
            elif nums[i] not in hash and k==0:
                hash[nums[i]] = 0
            

        return sum(hash.values())
		
		
'''
tricky solution.
(a + 2 = b) == (b-2=a) only need to consider one side. 
use build-in function collections.counter(nums). create hash table out of list 
'''
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k >0:
            return (len( set(nums) & set(i+k for i in nums)))
        elif k ==0:
            return(sum(val >1 for val in collections.Counter(nums).values()))
        else:
            return 0 


