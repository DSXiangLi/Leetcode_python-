"""
慢慢码系列 - Leetcode Python

404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


class Solution:
    def sumOfLeftLeaves(self,root):
        return self.sumOfLeftLeaves_recursion(root)
#        return self.sumOfLeftLeaves_DFS(root)

    def sumOfLeftLeaves_DFS(self, root):
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            tmp = stack.pop()
            if tmp.left:
                if not tmp.left.left and not tmp.left.right:
                    result += tmp.left.val
                else:
                    stack.append(tmp.left)
            if tmp.right: stack.append(tmp.right)
        return result

    def sumOfLeftLeaves_recursion(self, root):
        ## base case 1
        if not root:
            return 0
        ## base case 2 : left leaf
        if root.left and not root.left.left and not root.left.right:
            return self.sumOfLeftLeaves_recursion(root.right) + root.left.val
        return self.sumOfLeftLeaves_recursion(root.right) + self.sumOfLeftLeaves_recursion(root.left)

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
    result = Solution().sumOfLeftLeaves(p)
    print('Sum of left tree = {}'.format(result))

