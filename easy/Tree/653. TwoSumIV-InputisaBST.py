"""
慢慢码系列 - Leetcode Python
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number,
return true if there exist two elements in the
BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

## 依旧是inorder的应用, 并且存储之前遇到过的值和当前target-ndoe.val
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        self.allnode = set()
        self.found = False
        self.inorder_util(root, k)
        return self.found

    def inorder_util(self, root, k):
        if (not root) :
            return
        self.inorder_util(root.left, k)
        if (k - root.val) in self.allnode :
            self.found= True
            return
        self.allnode.add(root.val)
        self.inorder_util(root.right, k)


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
    target = int(input("Input your trage:"))
    p = StringToTreeNode(input_string);
    result = Solution().findTarget(p,target)
    print('Is there sum equal to target = {}'.format(result))

