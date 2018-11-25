"""
慢慢码系列 - Leetcode Python

234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Could you do it in O(n) time and O(1) space?
"""

##2种解法
# 直接把链表变成List，这个需要额外内存，虽然都是O（N）的时间但这个操作跟梢所以更快
# O(1) extra space, 反转后半部分的链表直接进行比较
class Solution(object):
    def isPalindrome(self, head):
#        return self.isPalindrome_list(head)
        return self.isPalindrome_link(head)

    def isPalindrome_link(self, head):
        # find mid point of linked list
        ptr_slow = head
        ptr_fast = head
        while ptr_fast and ptr_fast.next:
            ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next.next

        # reverse the second half of the linked list
        secondhalf = None
        while ptr_slow:
            tmp = ptr_slow
            ptr_slow = ptr_slow.next
            tmp.next = secondhalf
            secondhalf = tmp
        print("Reversed Seoncd half = {}".format(List2String(secondhalf)))
        while secondhalf:
            if head.val != secondhalf.val:
                return False
            secondhalf = secondhalf.next
            head = head.next
        return True

    def isPalindrome_list(self, head):
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return val == val[::-1]

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
    result = Solution().isPalindrome(linkedlist)
    print("Is linked list Palindrome = {}".format(result))
