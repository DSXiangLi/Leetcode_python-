"""
慢慢码系列 - Leetcode Python

530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
"""

##DFS 和 find mode 思路相同， 因为是BST所以应该利用inorder非递减的性质
##2种传递值的方式，递归返回值或者类的变量
class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getMinimumDifference_DFS(root)

    def getMinimumDifference_DFS(self, root):
        if not root:
            return 0
        _, min_diff = self.inorder_util(root, prev_node = None, min_diff = None)
        return min_diff

    def inorder_util(self, root, prev_node, min_diff):
        if root.left:
            prev_node, min_diff = self.inorder_util(root.left, prev_node, min_diff)
        if prev_node!= None:
            curr_diff = root.val - prev_node
            if (min_diff== None) or (curr_diff < min_diff):
                min_diff = curr_diff

        prev_node = root.val
        if root.right:
            prev_node, min_diff = self.inorder_util(root.right, prev_node, min_diff)

        return prev_node, min_diff

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
    result = Solution().getMinimumDifference(p)
    print('Minmial absolute difference of the tree = {}'.format(result))

0,null,2236,1277,2776,519