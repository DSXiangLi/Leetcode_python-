"""
慢慢码系列 - Leetcode Python

83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3新的链表应该指向一个None元素但不移动位置
## 当原始链表出现新的值的时候，新的链表指向新的值

Output: 1->2->3
"""
## 注意当原始链表值重复是，
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newlist = ListNode(head.val)
        ptr = newlist
        head = head.next
        while head:
            if ptr.val != head.val :
                ptr.next = head
                ptr = ptr.next
            else:
                ptr.next = None
            head = head.next
        return newlist

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
    result = Solution().deleteDuplicates(linkedlist)
    print("New linked list  = {}".format(List2String(result)))
