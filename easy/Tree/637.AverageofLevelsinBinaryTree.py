"""
慢慢码系列 - Leetcode Python

637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
 """
## 2种解题思路
##level order traversal
## recursion use level to keep track of the level
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return self.averageOfLevels_BFS(root)

    def averageOfLevels_BFS(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        level = 0
        while queue:
            num_item = len(queue)
            result.append(0)
            for i in range(num_item):
                tmp = queue.pop(0)
                result[level] += tmp.val
                print("Level = {}, result = {}, item ={}".format(level, result ,i ))

                if tmp.left: queue.append(tmp.left)
                if tmp.right: queue.append(tmp.right)
            result[level] = result[level]/num_item
            level +=1
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
    result = Solution().averageOfLevels(p)
    print('Average of each level in tree = {}'.format(result))

