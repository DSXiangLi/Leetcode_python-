"""
慢慢码系列 - Leetcode Python

572. Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

##
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        if self.issametree(s,t): return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    def issametree(self, s, t):
        if not s and not t:
            return True
        if ( s and not t) or (not s and t) or (s.val != t.val):
            return False
        return self.issametree(s.left, t.left) and self.issametree(s.right, t.right)

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
    input_string1 = input('Input your first string here (null): ')
    input_string2 = input('Input your second string here (null): ')

    p1 = StringToTreeNode(input_string1);
    p2 = StringToTreeNode(input_string2);

    result = Solution().isSubtree(p1,p2)
    print('IS t a subtree of s= {}'.format(result))

