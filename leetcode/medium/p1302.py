"""
recursive
m[depth] += root.val

return m[max(m.keys)]
"""
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.m = dict()
        self._f(root, 0)
        return self.m[max(self.m.keys())]

    def _f(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return

        self.m.setdefault(depth, 0)
        self.m[depth] += root.val
        self._f(root.left, depth + 1)
        self._f(root.right, depth + 1)

