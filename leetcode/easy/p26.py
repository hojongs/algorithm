"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[k] = nums[i]
                k += 1
                prev = nums[i]
        return k
