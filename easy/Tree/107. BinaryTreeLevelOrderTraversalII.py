"""
慢慢码系列 - Leetcode Python

107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
## 要点
#1.用List（mutatble）作为形参传入函数，List在函数外也会被修改因为mutable的数据类型传址不传值。
#2.如果函数需要记录递归过程中的变量，可以传入mutable的数据类型作为递归函数的形参
#3.如果是immutable的数据类型则需要使用全局变量
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
#        return self.levelOrderBottom_BFS(root)
        return self.levelOrderBottom_recursion(root)
    def levelOrderBottom_BFS(self,root):
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                tmp.append(node.val)
            result.append(tmp)
        return result[::-1]

    def levelOrderBottom_recursion(self, root):
        if not root:
            return []
        result = []
        self.recursion_util(root, 0, result)
        return result[::-1]

    def recursion_util(self, root, level, result):
        if not root: return
        if len(result) == level:
            result.append([])
        result[level].append(root.val)
        if root.left: self.recursion_util(root.left, level+1, result)
        if root.right: self.recursion_util(root.right, level+1, result)

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

    result = Solution().levelOrderBottom(p)
    print('Level order traversal result  = {}'.format(result))
