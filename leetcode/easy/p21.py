"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
알고리즘 강의 과제 코드 기억 그대로.. (왜 안 까먹을까)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        p1, p2, p3 = l1, l2, result

        while True:
            if p1 is None or p2 is None:
                break

            if p1.val <= p2.val:
                v = p1.val
                p1 = p1.next
            else:
                v = p2.val
                p2 = p2.next

            p3.next = ListNode(v)
            p3 = p3.next

        while p1 is not None:
            p3.next = ListNode(p1.val)
            p1 = p1.next
            p3 = p3.next
        while p2 is not None:
            p3.next = ListNode(p2.val)
            p2 = p2.next
            p3 = p3.next

        return result.next
