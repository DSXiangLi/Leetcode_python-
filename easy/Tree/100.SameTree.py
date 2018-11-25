"""
慢慢码系列 - Leetcode Python

100. Same Tree
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
#        return self.isSameTree_recursion(p,q)
#        return self.isSameTree_BFS(p,q)
        return self.isSameTree_DFS(p,q)
    def isSameTree_DFS(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if (node1 and node2 and node1.val != node2.val) or \
                (node1 and not node2) or (node2 and not node1):
                return False
            if node1 and node2:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True

    def isSameTree_BFS(self, p, q):
        queue = [(p,q)]
        while queue:
            for i in range(len(queue)):
                node1, node2 = queue.pop(0)
                if (node1 and node2 and node1.val != node2.val) or \
                    (node1 and not node2) or (node2 and not node1):
                        return False
                if node1 and node2:
                    queue.append((node1.left, node2.left))
                    queue.append((node1.right, node2.right))
        return True

    def isSameTree_recursion(self, p, q):
        ## Base case
        if not p and not q:
            return True
        ## when to stop
        if (not p and q) or (not q and p) or (p and q and p.val != q.val) :
            return False
        ## how to call itself
        return self.isSameTree_recursion(p.left, q.left) and self.isSameTree_recursion(p.right, q.right)


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
    p = StringToTreeNode(input_string1);
    q = StringToTreeNode(input_string2);

    result = Solution().isSameTree(p, q)
    print('Are they the same? {}'.format(result))
