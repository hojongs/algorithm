"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

10초컷
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i

        return len(nums)
