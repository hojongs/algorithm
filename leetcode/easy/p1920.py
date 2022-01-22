"""
1920. Build Array from Permutation
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        for i, n in enumerate(nums):
            result[i] = nums[n]
        return result
