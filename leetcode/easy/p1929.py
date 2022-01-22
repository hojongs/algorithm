"""
1929. Concatenation of Array
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
