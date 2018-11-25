"""
慢慢码系列 - Leetcode Python

226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

##这里又用到TreeNode也是mutable的数据类型，所以传址不传值
##递归过程只是调用自身函数并没有返回值，返回值用在Base case终止时

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#        return self.invertTree_recursion(root)
        return self.invertTree_DFS(root)
    def invertTree_recursion(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree_DFS(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            tmp = stack.pop()
            tmp.left, tmp.right = tmp.right,tmp.left
            if tmp.left: stack.append(tmp.left)
            if tmp.right: stack.append(tmp.right)
        return root

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
    input_string = input('Input your tree here (null): ')
    p = StringToTreeNode(input_string);
    print('Original Tree  = {}'.format(Solution().levelOrderBottom_BFS(p)))
    Solution().invertTree(p)
    print('Inverted Tree  = {}'.format(Solution().levelOrderBottom_BFS(p)))
