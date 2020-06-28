"""
慢慢码系列 - Leetcode Python

590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            result.append(tmp.val)
            stack += [i for i in tmp.children if tmp.children]
        return result[::-1]


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
