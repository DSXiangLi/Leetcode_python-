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

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetric_recursion(root)
    def isSymmetric_recursion(self, root):
        ## base case
        if (not root) :
            return True
        return self.isSymmetric2(root.left, root.right)

    def isSymmetric2(self, node1, node2):
        ## when to stop 1
        if (not node1) and (not node2):
            return True
        ## when to stop2
        if (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
            return False
        return self.isSymmetric2(node1.left, node2.right) and self.isSymmetric2(node1.right,node2.left)

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
    input_string = input('Input your first tree here (null): ')
    p = StringToTreeNode(input_string);
    result = Solution().isSymmetric(p)
    print('Is tree symmetric? {}'.format(result))
