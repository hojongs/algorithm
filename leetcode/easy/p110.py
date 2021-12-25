"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Time Complexity:
Space Complexity: O(1)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        b = abs(get_height(root.left) - get_height(root.right)) <= 1
        return b and self.isBalanced(root.left) and self.isBalanced(root.right)


def get_height(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1
