"""
慢慢码系列 - Leetcode Python

270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

class Solution(object):
    def closetValue(self,root, target):
        return self.closetValue_BFS(root, target)
#        return self.closetValue_recursion(root, target)

    def closetValue_BFS(self, root, target):
        if not root:
            return None
        result = root.val
        gap = target - result
        while True:
            print(result)
            print(gap)
            if gap == 0:
                return result
            elif gap>0:
                if root.right and gap > abs(root.right.val - target):
                    root = root.right
                    result = root.val
                    gap = target - result
                else:
                    break;
            else:
                if root.left and abs(gap) > abs(root.left.val - target):
                    root = root.left
                    result = root.val
                    gap = target - result
                else:
                   break;
        return result
    def closetValue_recursion(self, root, target):
        if not root:
            return None
        if target == root.val:
            return root.val
        elif target > root.val:
            return self.closestValue_recursion(root.right, target, root.val)
        else:
            return self.closestValue_recursion(root.left, target, root.val)

    def recursion_util(self, root, target, prev_val):
        if not root:
            return prev_val
        if target == root.val:
            return root.val
        elif target > root.val:
            if target < prev_val:
                if abs(target - prev_val) < abs(target - root.val):
                    return prev_val
                else:
                    return root.val
            else:
                return self.closestValue_recursion(root.right, target, root.val)
        else:
            if target < prev_val:
                return self.closestValue_recursion(root.left, target, root.val)
            else:
                if abs(target - prev_val) < abs(target - root.val):
                    return prev_val
                else:
                    return root.val


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
    target = int(input("input your target here: "))
    p = StringToTreeNode(input_string);
    result = Solution().closetValue(p, target)
    print('The cloest value to your target is  {}'.format(result))
