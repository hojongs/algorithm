"""
116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Algorithm abstract (Key idea):
The next node of a node can be found:
If the node is left, then parent->right
Else (right), then parent->next->left
Connecting next nodes should be done in pre-order
"""


# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None

        self.f(root.left, True, root)
        self.f(root.right, False, root)
        return root

    def f(self, current: Optional['Node'], is_left: bool, parent: Optional['Node']):
        if current is None:
            return

        if is_left:
            if parent is not None:
                current.next = parent.right
        else:
            if parent is not None and parent.next is not None:
                current.next = parent.next.left
        self.f(current.left, True, current)
        self.f(current.right, False, current)
