"""
慢慢码系列 - Leetcode Python

257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

##又一次遇到遍历树并且需要按照特定顺序返回所有节点值,2种记录节点的方法
#1.用全局变量
#2.传递mutable的List,List作为形参传入递归函数，函数不返回值而是在递归过程中修改List
## 需要注意的是每次一递归写入的是当前节点的值所以Base Case就不再是当前节点是否为空，而是当前节点是否为叶节点
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
#        return self.binaryTreePaths_recursion1(root)
        return self.binaryTreePaths_recursion2(root)

    def binaryTreePaths_recursion1(self,root):
        if not root:
            return []
        result = []
        path = str(root.val)
        self.recursion_util1(root, path, result)
        return result

    def recursion_util1(self, root, path, result):
        if not root.left and not root.right:
            result.append(path)
        if root.left : self.recursion_util1(root.left, path + "->" + str(root.left.val), result)
        if root.right: self.recursion_util1(root.right, path + "->" + str(root.right.val), result)

    def binaryTreePaths_recursion2(self,root):
        if not root:
            return []
        self.result = []
        path = str(root.val)
        self.recursion_util2(root,path)
        return self.result

    def recursion_util2(self, root, path):
        if not root.left and not root.right:
            self.result.append(path)
        if root.left : self.recursion_util2(root.left, path + "->" + str(root.left.val))
        if root.right: self.recursion_util2(root.right, path + "->" + str(root.right.val))



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
    input_string = input('Input your tree here (null): ')
    p = StringToTreeNode(input_string);
    print('All the Tree paths  = {}'.format(Solution().binaryTreePaths(p)))
