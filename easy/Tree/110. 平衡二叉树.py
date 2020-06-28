"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right))>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if not node:
            return 0

        return max(self.depth(node.left), self.depth(node.right)) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.check = True
        def helper(root):
            if not root:
                return 0
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            if abs(left_depth - right_depth) >1:
                self.check = False

            return max(left_depth, right_depth) + 1

        helper(root)
        return self.check