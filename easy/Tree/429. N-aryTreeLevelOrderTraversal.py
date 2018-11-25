"""
慢慢码系列 - Leetcode Python

429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            tmp_list = []
            for i in range(len(queue)):
                tmp_node = queue.pop(0)
                queue += [i for i in tmp_node.children if tmp_node.children]
                tmp_list.append(tmp_node.val)
            result.append(tmp_list)
        return result

