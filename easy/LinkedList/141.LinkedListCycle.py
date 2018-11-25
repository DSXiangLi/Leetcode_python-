"""
慢慢码系列 - Leetcode Python

141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
# Tricky 的部分在于如果链表有闭环那无论怎么移动指针都不会结束
# 只要两个指针移动速度不一样总会相遇，就像小学追击问题距离是环的长度
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr_slow = head
        ptr_fast = head
        while ptr_fast and ptr_fast.next:
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next
            if ptr_slow == ptr_fast:
                return True
        return False
