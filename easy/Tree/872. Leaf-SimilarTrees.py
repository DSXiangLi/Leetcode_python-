"""
慢慢码系列 - Leetcode Python

872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Note:

Both of the given trees will have between 1 and 100 nodes.
"""

###DFS to get all leafs.
# use the mutable list as parameter.
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        leaf1 = self.getleaf(root1, [])
        leaf2 = self.getleaf(root2,[])

        return leaf1 == leaf2

    def getleaf(self, root, leafs):
        if not root:
            return
        if not root.left and not root.right:
            leafs.append(root.val)
        self.getleaf(root.left, leafs)
        self.getleaf(root.right, leafs)
        return leafs


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
    input_string1 = input('Input your first string here (null): ')
    input_string2 = input('Input your second string here (null): ')

    p1 = StringToTreeNode(input_string1);
    p2 = StringToTreeNode(input_string2);
    result = Solution().leafSimilar(p1,p2)
    print('Do they have similar leafs = {}'.format(result))
