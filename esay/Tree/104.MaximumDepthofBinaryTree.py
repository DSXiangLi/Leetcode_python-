'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def maxDepth(self, root):
		if not root:
			return 0 
			
		left = self.maxDepth(root.left) + 1 
		right = self.maxDepth(root.right) + 1
		
		return max(left, right )