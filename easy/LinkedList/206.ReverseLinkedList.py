"""
慢慢码系列 - Leetcode Python

206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
##反转链表
#1.指针1遍历原始链表
#2.新的链表是从尾部开始构建，从一个指向None的几点
#3.一个临时变量用于反转没给原始链表的节点
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newlist = None
        while head:
            tmp = head # 提取原始链表每一个节点
            head = head.next # 移动原始链表指针去下一个节点
            tmp.next = newlist # 反转该节点
            newlist = tmp # 移动新链表到到当前地址， 这里是从尾到头反着移动
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
    result = Solution().reverseList(linkedlist)
    print("Reversed linked list  = {}".format(List2String(result)))
