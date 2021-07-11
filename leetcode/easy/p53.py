"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        my_sum = 0
        max_sum = -inf
        for i, v in enumerate(nums):
            my_sum += v
            my_sum = max(my_sum, v)
            max_sum = max(max_sum, my_sum)
        return max_sum
