'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
'''

'''
Trick: since the path doesn't need to be from root to the bottom. at each level we can choose to include current level or not.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
			return 0
			
		return (root.val == sum ? 1:0) + \
		self.pathSum(root.left, sum) + self.pathSum(root.left, sum - root.val) +\
		self.pathSum(root.right, sum) + self.pathSum(root.right, sum - root.val) 