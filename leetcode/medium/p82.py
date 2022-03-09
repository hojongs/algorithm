"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
"""


# Definition for a Node.
from typing import Optional

from leetcode.medium.util import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        head2 = ListNode()
        curr2 = head2
        while curr is not None:
            # if curr == next (duplicated)
            # go to next number
            if curr.next is not None and curr.val == curr.next.val:
                val = curr.val
                while curr is not None and curr.val == val:
                    curr = curr.next
            # else
            # add and next
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
                curr = curr.next
        return head2.next
