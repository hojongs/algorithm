"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        head = ListNode(next=head)

        prev = head
        curr = head.next
        while curr.next is not None:
            if curr.val == curr.next.val:
                # remove node
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head.next
