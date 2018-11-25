"""
慢慢码系列 - Leetcode Python

538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original
key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

##和find mode, min difference 思路相反,反转inorder返回非递减序列，以及之前所有节点的和
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.cumsum = 0
        return self.DFS_util(root)

    def DFS_util(self, root):
        # right
        if not root:
            return
        self.DFS_util(root.right)
        # root
        cursum = self.cumsum
        self.cumsum += root.val
        root.val += cursum
        # left
        self.DFS_util(root.left)
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
        return result

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
    print('Original Tree= {}'.format(Solution().levelOrderBottom_BFS(p)))
    Solution().convertBST(p)
    print('Bigger Tree= {}'.format(Solution().levelOrderBottom_BFS(p)))

