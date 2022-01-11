"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.__f(root, result)
        return result

    def __f(self, root: Optional[TreeNode], result: List[int]):
        if root is not None:
            result.append(root.val)
            self.__f(root.left, result)
            self.__f(root.right, result)
