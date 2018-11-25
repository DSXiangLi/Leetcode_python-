"""
慢慢码系列 - Leetcode Python

110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
"""
## 和max depth的基本逻辑相同，有2点比较tricky
# 1. 递归函数的返回值是一致的，如何能同时返回当前树的最大深度并同时返回是否平衡？ 试试把深度设为-1
# 2. 递归函数无法中途跳出，所以要记得把是否平衡的判断一直传递下去
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.postorder_util(root) >0

    def postorder_util(self,root):
        if not root:
            return 0
        left = self.postorder_util(root.left)
        right = self.postorder_util(root.right)
        if abs(left-right)>1 or left ==-1 or right == -1:
            return -1
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
    result = Solution().isBalanced(p)
    print('Is the tree balanced ? {}'.format(result))