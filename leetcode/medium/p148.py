"""
148. Sort List
https://leetcode.com/problems/sort-list/

Merge sort로 구현
Merge sort 리마인드 (몇 년만에..): partition to left,right -> merge sort respectively, merge into one
시간나면 나중에 inPlace로 구현 (bottom up)
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        head = ListNode(next=head)
        # partition
        p = head.next
        p2 = head
        while p is not None and p.next is not None:
            p = p.next.next
            p2 = p2.next
        mid = p2.next
        p2.next = None

        # merge sort
        h1 = self.sortList(head.next)
        h2 = self.sortList(mid)

        # merge
        head2 = ListNode()
        p1, p2, p3 = h1, h2, head2
        while True:
            if p1 is None or p2 is None:
                break

            if p1.val <= p2.val:
                p3.next = ListNode(p1.val)
                p3 = p3.next
                p1 = p1.next
            else:
                p3.next = ListNode(p2.val)
                p3 = p3.next
                p2 = p2.next

        while p1 is not None:
            p3.next = ListNode(p1.val)
            p3 = p3.next
            p1 = p1.next
        while p2 is not None:
            p3.next = ListNode(p2.val)
            p3 = p3.next
            p2 = p2.next

        return head2.next

    """
    Selection Sort: O(n^2), Time limit exceeded
    Linked List sorting 시 head node가 있으면 로직이 간단해진다
    Selection sort는 간단히 표현하면 n을 알고 있을 때, find min (O(n)) -> pop&append min n번(O(n)) 반복이다
    """
    # def sortList_sel(self, head: ListNode) -> ListNode:
    #     # add head node
    #     head = ListNode(next=head)
    #     # find cnt
    #     cnt = 0
    #     p = head.next
    #     while p is not None:
    #         cnt += 1
    #         p = p.next
    #
    #     # get sorted
    #     head2 = ListNode()
    #     p2 = head2
    #     i = 0
    #     while i < cnt:
    #         # find min node
    #         p = head.next
    #         min_prev_p = head
    #         min_p = head.next
    #         while p.next is not None:
    #             if p.next.val < min_p.val:
    #                 min_prev_p = p
    #                 min_p = p.next
    #             p = p.next
    #         # append min node
    #         p2.next = ListNode(min_p.val)
    #         p2 = p2.next
    #         min_prev_p.next = min_p.next
    #         i += 1
    #
    #     return head2.next


a = Solution().sortList(ListNode(4, ListNode(2, ListNode(3, ListNode(1)))))
while a is not None:
    print(a.val)
    a = a.next
a = Solution().sortList(ListNode(-1, ListNode(2, ListNode(3))))
while a is not None:
    print(a.val)
    a = a.next
a = Solution().sortList(ListNode(-1, ListNode(2, ListNode(3, ListNode(1)))))
while a is not None:
    print(a.val)
    a = a.next
