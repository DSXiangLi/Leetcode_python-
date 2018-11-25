"""
慢慢码系列 - Leetcode Python

563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.

"""

## post order traversal，先经过左/右节点累加差的绝对值，回到根节点结算子树所有节点的和，然后重复
class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.postorder_util(root)
        return self.tilt
    def postorder_util(self,root):
        if not root:
            return 0
        ## 递归顺序
        # 左
        left = self.postorder_util(root.left)
        # 右
        right = self.postorder_util(root.right)
        # 重复步骤
        self.tilt += abs( left- right)
        # 回到根节点
        return root.val + left + right

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
        ## create l eft node add to the queue
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
    print('Tilt of  tree = {}'.format(Solution().findTilt(p)))

