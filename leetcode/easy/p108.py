"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Algorithm Abstract: Divide & Conquer
Split the nums list to left, mid, right
Make the left to left tree by calling the algorithm recursively, and do the same thing for the right tree
Return root node with the value of the mid and left tree and right tree

Comment:
알고리즘 꾸준히 풀어야겠다 (뇌가 굳었다)
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.f(nums, 0, len(nums) - 1)

    def f(self, nums: List[int], first_idx: int, last_idx: int) -> Optional[TreeNode]:
        cnt = last_idx - first_idx + 1
        if cnt <= 0:
            return None
        elif cnt == 1:
            return TreeNode(nums[first_idx])

        mid_idx = (first_idx + last_idx + 1) // 2
        left = self.f(nums, first_idx, mid_idx - 1)
        right = self.f(nums, mid_idx + 1, last_idx)
        return TreeNode(nums[mid_idx], left=left, right=right)
