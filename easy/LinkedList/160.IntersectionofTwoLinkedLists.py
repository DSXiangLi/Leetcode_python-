"""
慢慢码系列 - Leetcode Python

160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection
 of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
"""
# 这题比较Tricky有技巧的解法是对两个List进行交叉检验
# A -> A+ B
# B -> B+ A
# 这样短的链表先拼接长的链表，长的链表后拼接段的链表
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        return self.iteration_util(headA, headB)
    def iteration_util(self, headA, headB):
        if not headA:
            return None
        if not headB:
            return None
        ptrA = headA
        ptrB = headB
        while (ptrA or ptrB):
            ## 拼接列表使得A，B拥有相同长度
            if not ptrA:
                ptrA = headB
            if not ptrB:
                ptrB = headA
            if ptrA.val == ptrB.val:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next

        return None

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
    result = Solution().getIntersectionNode(linkedlist1,linkedlist2)
    print("The intersection of 2 linked list  = {}".format(List2String(result)))
