"""
慢慢码系列 - Leetcode Python

501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.



For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].
Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""
## 2种解法
#1. Hash table解法
#2. Preorder解法，BST preorder会返回非递减序列，所以只需要判断当前值是否和上一个值相同。
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#        return self.findMode_hash(root)
        return self.findMode_DFS(root)
    def findMode_hash(self,root):
        if not root:
            return []
        self.hash = dict()
        self.recursion_util(root)
        max_count = max(self.hash.values())
        return [key for key,value in self.hash.items() if value == max_count]

    def recursion_util(self,root):
        if not root:
            return
        self.hash[root.val] = self.hash.get(root.val, 0) + 1
        self.recursion_util(root.left)
        self.recursion_util(root.right)

    def findMode_preorder(self, root):
        if not root:
            return []
        self.mode = []
        max_count, curr_count, prev_node = self.inorder_util(root, max_count =0 , curr_count = None , prev_node =None)
        return self.mode

    def inorder_util(self, root, max_count, curr_count, prev_node):
        ## judge on left node
        if root.left:
            max_count, curr_count, prev_node = self.inorder_util(root.left, max_count, curr_count, prev_node)
        ## judge on root node
        if root.val == prev_node:
            curr_count +=1
        else:
            curr_count = 1
            prev_node = root.val			
        if curr_count > max_count:
            self.mode = [root.val]
            max_count = curr_count
        elif curr_count == max_count:
            self.mode.append(root.val)
        ## judge on right node
        if root.right:
            max_count, curr_count, prev_node = self.inordre_util(root.right, max_count, curr_count, prev_node)
        return max_count, curr_count, prev_node


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
    result = Solution().findMode(p)
    print('The mode of tree = {}'.format(result))

