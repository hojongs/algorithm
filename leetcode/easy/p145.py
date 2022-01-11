"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

TODO: iterative solution
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.__f(root, result)
        return result

    def __f(self, root: Optional[TreeNode], result: List[int]):
        if root is not None:
            self.__f(root.left, result)
            self.__f(root.right, result)
            result.append(root.val)
