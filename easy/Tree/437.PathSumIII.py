"""
慢慢码系列 - Leetcode Python

437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
##这题我一直有问题因为在递归时只考虑了每个节点可以减也可以不减，但这样就会出现跳跃
## 正确解法应该是在任意节点上重复PathSum的逻辑
## 还有要注意这里不简单返回1因为当当前节点满足条件后，继续往下走还有可能有新的路径，如果返回该路径就会终止

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.pathSum_recursion(root,sum)
        return self.result
    def pathSum_recursion(self, root, sum):
        if not root:
            return 0
        self.recursion_util(root, sum)
        self.pathSum_recursion(root.left,sum)
        self.pathSum_recursion(root.right,sum)
        return self.result
    def recursion_util(self, root, sum):
        ## 这一部分和pathSum的逻辑一致
        if not root:
            return
        if root.val == sum:
            self.result +=1
        self.recursion_util(root.left, sum - root.val)
        self.recursion_util(root.right, sum - root.val)

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
    target = int(input("Input your target here: "))
    p = StringToTreeNode(input_string);
    result = Solution().pathSum(p, target)
    print('Sum of left tree = {}'.format(result))

