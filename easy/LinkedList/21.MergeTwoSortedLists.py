"""
慢慢码系列 - Leetcode Python

21. Merge Two Sorted Lists


Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
#linked list 注意指针问题记得保留初始地址用于返回值

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#        return self.recursion_util(l1,l2)
        return self.iteration_util(l1,l2)
    def recursion_util(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        if l1.val < l2.val:
            merghead = l1
            merghead.next = self.recursion_util(l1.next, l2)
        else:
            merghead = l2
            merghead.next = self.recursion_util(l1,l2.next)
        return merghead

    def iteration_util(self, l1,l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        mergehead  = ListNode(0)
        ptr = mergehead
        while l1 or l2:
            if not l1:
                ptr.next = l2
                break
            if not l2:
                ptr.next = l1
                break
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        return mergehead.next

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
    string1 = input("Input your list element here:")
    linkedlist1 = String2List(string1)
    string2 = input("Input your list element here:")
    linkedlist2 = String2List(string2)
    print("First linlked list = {}".format(List2String(linkedlist1)))
    print("Second linlked list = {}".format(List2String(linkedlist2)))
    result = Solution().mergeTwoLists(linkedlist1,linkedlist2)
    print("Merged linlked list = {}".format(List2String(result)))
