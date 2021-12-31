# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        p = head # primary
        s = head # secondary
        i = 0

        while True:
            if i == 0:
                p = p.next
            else:
                p = p.next
                s = s.next

            if p is None:
                return False
            elif p == s:
                return True

            i = i^1

