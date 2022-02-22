"""

"""
from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new = ListNode()
        newp = new
        p = head.next
        while p is not None:
            v = 0
            while p.val != 0:
                v += p.val
                p = p.next
            newp.next = ListNode(v)
            newp = newp.next
            p = p.next
        return new.next

