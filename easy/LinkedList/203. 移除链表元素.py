"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newlist = ListNode(0)
        ptr = newlist
        while head:
            if head.val != val:
                ptr.next = head
                ptr = ptr.next
            else:
                ptr.next = None # 删掉原始链表之后的部分
            head = head.next

        return newlist.next

