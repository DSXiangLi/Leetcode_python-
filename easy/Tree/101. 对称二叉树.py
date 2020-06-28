"""
慢慢码系列 - Leetcode Python

101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs( node_left, node_right):
            if (not node_left) and (not node_right):
                return True
            elif (not node_left) and node_right:
                return False
            elif (node_left) and (not node_right):
                return False
            elif node_left.val != node_right.val:
                return False
            else:
                return dfs(node_left.left, node_right.right) and dfs(node_left.right, node_right.left)

        if not root:
            return True
        return dfs(root.left, root.right)