"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return []

        def helper(root, path):
            if (not root.left) and (not root.right):
                result.append( path + [str( root.val )] )
            if root.left:
                helper( root.left, path + [str( root.val )] )
            if root.right:
                helper( root.right, path + [str( root.val )] )

        helper( root, [] )

        return ['->'.join( i ) for i in result]

