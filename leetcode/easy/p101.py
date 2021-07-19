"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        return self.isSame(root.left, root.right)

    def isSame(self, a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False

        if a.val != b.val:
            return False
        if not self.isSame(a.left, b.right):
            return False
        if not self.isSame(a.right, b.left):
            return False

        return True
