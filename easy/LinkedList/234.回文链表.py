"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 列表解法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ll = []
        while head:
            ll.append(head.val)
            head = head.next

        return ll == ll[::-1]



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slowptr = head
        fastptr = head
        while (fastptr and fastptr.next):
            slowptr = slowptr.next
            fastptr = fastptr.next.next

        # slowptr is at the mid point: reverse second half
        newptr = None
        while slowptr:
            tmp = slowptr.next
            slowptr.next = newptr
            newptr = slowptr
            slowptr = tmp

        # compare 1st & 2nd half
        while newptr:
            if newptr.val != head.val:
                return False
            newptr = newptr.next
            head = head.next

        return True