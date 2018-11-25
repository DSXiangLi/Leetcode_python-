"""
慢慢码系列 - Leetcode Python

104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

## BFS is faster than recursion
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#        return self.maxDepth_BFS(root)
        return self.maxDepth_recursion(root)
    def maxDepth_BFS(self, root):
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue :
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)
            level +=1
        return level

    def maxDepth_recursion(self, root):
        ## when to stop
        if not root:
            return 0
        ## how to call it self
        left = self.maxDepth_recursion(root.left)
        right = self.maxDepth_recursion(root.right)
        return max(left, right) + 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def StringToTreeNode(string):
    items = [i for i in string.split(",")]
    root = TreeNode(int(items[0]))
    nodeq = [root]
    item_count = 1
    node_count = 0

    while item_count < len(items):
        node = nodeq[node_count]
        node_count +=1
        ## create left node add to the queue
        if items[item_count]!='null':
            node.left = TreeNode(int(items[item_count]))
            nodeq.append(node.left)

        item_count +=1
        if node_count >=len(items):
            break
        ## create right node add to the queue
        if items[item_count]!='null':
            node.right = TreeNode(int(items[item_count]))
            nodeq.append(node.right)
        item_count +=1
    return root

def main():
    input_string = input('Input your first string here (null): ')
    p = StringToTreeNode(input_string);

    result = Solution().maxDepth(p)
    print('Max Depth of tree = {}'.format(result))
