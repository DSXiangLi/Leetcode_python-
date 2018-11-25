"""
慢慢码系列 - Leetcode Python

203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""
## 2 个指针一个指向新的链表，一个指向原始链表
## 如果当前值保留则新链表指向原始链表，两个链表同时移到下一位
## 如果当前值删除则新链表指向原始的下一位，只移动原始链表
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newlist = ListNode(0)
        ptr = newlist
        while head:
            if head.val == val:
                ptr.next = None
            else:
                ptr.next = head
                ptr = ptr.next
            head = head.next

        return newlist.next

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
    target = int(input("Input your removed element here:"))
    print("Original linked list  = {}".format(List2String(linkedlist)))
    result = Solution().removeElements(linkedlist, target)
    print("New linked list  = {}".format(List2String(result)))
