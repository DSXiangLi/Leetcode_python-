"""
慢慢码系列 - Leetcode Python

108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        ## base case
        if not nums:
            return None
        ## single step
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[(mid+1):])
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

def main():
    input_string = input('Input your element here  here (null): ')
    num = [int(i) if i !='null' else i for i in input_string.split(",")]
    Tree = Solution().sortedArrayToBST(num)

    print('Return level order traversal of the tree {}'.format(Solution().levelOrderBottom_BFS(Tree)))
