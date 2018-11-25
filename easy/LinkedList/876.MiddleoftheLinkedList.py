"""
慢慢码系列 - Leetcode Python

876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.


Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.
"""
## 和find cycle 问题类似这里也是用连个指针当快指针到达末尾时慢指针刚好的中间


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr_slow = head
        ptr_fast = head
        while ptr_fast and ptr_fast.next:
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next
        return ptr_slow

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def String2List(string):
    items = [int(i) for i in string.split(",")]
    linkedlist = ListNode(0)
    ptr = linkedlist
    for i in range(len(items)):
         ptr.next= ListNode(items[i])
         ptr = ptr.next
    return linkedlist.next

def List2String(linkedlist):
    items = str(linkedlist.val)
    linkedlist = linkedlist.next
    while linkedlist:
        items += '->' + str(linkedlist.val)
        linkedlist = linkedlist.next
    return items


def main():
    string = input("Input your list element here:")
    linkedlist = String2List(string)
    print("Original linked list  = {}".format(List2String(linkedlist)))
    result = Solution().middleNode(linkedlist)
    print("Middle of linked list  = {}".format(List2String(result)))
