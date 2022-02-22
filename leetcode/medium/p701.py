"""
701. Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""
# Definition for a Node.
from typing import Optional

from tree_node import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        return root

